# Activity onSaveInstanceState() 方法分析
- 2016-03-22 03:47:26
- 
- 

<!--markdown-->Activity 的 onSaveInstanceState() 方法不同于生命周期的其他方法，但是它会在 Actvitity 可能被销毁的情况下，保存一些界面布局的信息，以便在下次恢复的时候能够回到之前的状态。那么这里有几个东西咱们需要知道的。
1. 什么时候被执行
2. 哪些信息被保存
3. 它是怎么保存的
4. 如何恢复

这里咱们主要看的是第三点，也就是它是怎么工作的，下面是从 Activity 的 onSaveInstanceState() 方法一路追踪下去的分析。


<!--more-->


首先是 Actvitity，咱们看看 Activity 都干了什么。这个方法有个核心的对象是 mFragments ，它是FragmentManager 的一个实例。

    protected void onSaveInstanceState(Bundle outState) {
        outState.putBundle(WINDOW_HIERARCHY_TAG, mWindow.saveHierarchyState());
        // mFragments 是 FragmentManager 对象
        Parcelable p = mFragments.saveAllState();
        if (p != null) {
            outState.putParcelable(FRAGMENTS_TAG, p);
        }
        getApplication().dispatchActivitySaveInstanceState(this, outState);
    }

FragmentManager 是一个抽象类，它的实现是 FragmentManagerImpl , 是 FragmentManager 的一个内部类，它实现了 saveAllState() 方法。

FragmentManager 的代码：

    Parcelable saveAllState() {
        // Make sure all pending operations have now been executed to get
        // our state update-to-date.
        execPendingActions();

        mStateSaved = true;

        if (mActive == null || mActive.size() <= 0) {
            return null;
        }
        
        // First collect all active fragments.第一步收集的是 active 的 fragments
        int N = mActive.size();
        FragmentState[] active = new FragmentState[N];
        boolean haveFragments = false;
        // 遍历 fragments
        for (int i=0; i<N; i++) {
            Fragment f = mActive.get(i);
            if (f != null) {
                if (f.mIndex < 0) {
                    throwException(new IllegalStateException(
                            "Failure saving state: active " + f
                            + " has cleared index: " + f.mIndex));
                }

                haveFragments = true;

                FragmentState fs = new FragmentState(f);
                active[i] = fs;
                
                if (f.mState > Fragment.INITIALIZING && fs.mSavedFragmentState == null) {
                    // mSavedFragmentState 是一个 bundle 对象
                    fs.mSavedFragmentState = saveFragmentBasicState(f);

                    if (f.mTarget != null) {
                        if (f.mTarget.mIndex < 0) {
                            throwException(new IllegalStateException(
                                    "Failure saving state: " + f
                                    + " has target not in fragment manager: " + f.mTarget));
                        }
                        if (fs.mSavedFragmentState == null) {
                            fs.mSavedFragmentState = new Bundle();
                        }
                        putFragment(fs.mSavedFragmentState,
                                FragmentManagerImpl.TARGET_STATE_TAG, f.mTarget);
                        if (f.mTargetRequestCode != 0) {
                            fs.mSavedFragmentState.putInt(
                                    FragmentManagerImpl.TARGET_REQUEST_CODE_STATE_TAG,
                                    f.mTargetRequestCode);
                        }
                    }

                } else {
                    fs.mSavedFragmentState = f.mSavedFragmentState;
                }
                
                if (DEBUG) Log.v(TAG, "Saved state of " + f + ": "
                        + fs.mSavedFragmentState);
            }
        }
        
        if (!haveFragments) {
            if (DEBUG) Log.v(TAG, "saveAllState: no fragments!");
            return null;
        }
        
        int[] added = null;
        BackStackState[] backStack = null;
        
        // Build list of currently added fragments.
        if (mAdded != null) {
            N = mAdded.size();
            if (N > 0) {
                added = new int[N];
                for (int i=0; i<N; i++) {
                    added[i] = mAdded.get(i).mIndex;
                    if (added[i] < 0) {
                        throwException(new IllegalStateException(
                                "Failure saving state: active " + mAdded.get(i)
                                + " has cleared index: " + added[i]));
                    }
                    if (DEBUG) Log.v(TAG, "saveAllState: adding fragment #" + i
                            + ": " + mAdded.get(i));
                }
            }
        }
        
        // Now save back stack.
        if (mBackStack != null) {
            N = mBackStack.size();
            if (N > 0) {
                backStack = new BackStackState[N];
                for (int i=0; i<N; i++) {
                    backStack[i] = new BackStackState(this, mBackStack.get(i));
                    if (DEBUG) Log.v(TAG, "saveAllState: adding back stack #" + i
                            + ": " + mBackStack.get(i));
                }
            }
        }
        
        FragmentManagerState fms = new FragmentManagerState();
        fms.mActive = active;
        fms.mAdded = added;
        fms.mBackStack = backStack;
        return fms;
    }

这个方法还有点长，咱们可以看到它都保存了什么东西。First collect all active fragments.它的注释就这样写的，先保存活动着的 fragments，然后会调用 saveFragmentBasicState(f) ，返回一个 bundle 对象，下面我们看看 saveFragmentBasicState(Fragment f) 这个方法。

    Bundle saveFragmentBasicState(Fragment f) {
        Bundle result = null;

        if (mStateBundle == null) {
            mStateBundle = new Bundle();
        }
        f.performSaveInstanceState(mStateBundle);
        if (!mStateBundle.isEmpty()) {
            result = mStateBundle;
            mStateBundle = null;
        }
        //这里是咱们要看的
        if (f.mView != null) {
            saveFragmentViewState(f);
        }
        if (f.mSavedViewState != null) {
            if (result == null) {
                result = new Bundle();
            }
            result.putSparseParcelableArray(
                    FragmentManagerImpl.VIEW_STATE_TAG, f.mSavedViewState);
        }
        if (!f.mUserVisibleHint) {
            if (result == null) {
                result = new Bundle();
            }
            // Only add this if it's not the default value
            result.putBoolean(FragmentManagerImpl.USER_VISIBLE_HINT_TAG, f.mUserVisibleHint);
        }

        return result;
    }

在这个方法里，如果 f.mView != null , 那么调用 saveFragmentViewState(f) 方法。saveFragmentViewState() 方法里，会实例化一个 SparseArray<Parcelable> 对象，然后调用 f.mView.saveHierarchyState(mStateArray) 方法。 

    void saveFragmentViewState(Fragment f) {
        if (f.mView == null) {
            return;
        }
        //这里准备了一个 SparseArray ，用来保存数据
        if (mStateArray == null) {
            mStateArray = new SparseArray<Parcelable>();
        } else {
            mStateArray.clear();
        }
        //这里开始保存数据到 SparseArray
        f.mView.saveHierarchyState(mStateArray);
        if (mStateArray.size() > 0) {
            f.mSavedViewState = mStateArray;
            mStateArray = null;
        }
    }

这里，它初始化了一个 SparseArray，应该就是用来保存数据用的，然后我们去看看View.saveHierarchyState() 方法。

    public void saveHierarchyState(SparseArray<Parcelable> container) {
        dispatchSaveInstanceState(container);
    }

View.saveHierarchyState() 方法直接调用 dispatchSaveInstanceState(container) ，然后我们看看 dispatchSaveInstanceState(container) 方法。

    protected void dispatchSaveInstanceState(SparseArray<Parcelable> container) {
        if (mID != NO_ID && (mViewFlags & SAVE_DISABLED_MASK) == 0) {
            mPrivateFlags &= ~PFLAG_SAVE_STATE_CALLED;
            Parcelable state = onSaveInstanceState();
            if ((mPrivateFlags & PFLAG_SAVE_STATE_CALLED) == 0) {
                throw new IllegalStateException(
                        "Derived class did not call super.onSaveInstanceState()");
            }
            if (state != null) {
                // Log.i("View", "Freezing #" + Integer.toHexString(mID)
                // + ": " + state);
                container.put(mID, state);
            }
        }
    }

这里我们可以看到，如果 mID != NO_ID ,那么会调用 onSaveInstanceState() 方法。

    protected Parcelable onSaveInstanceState() {
        mPrivateFlags |= PFLAG_SAVE_STATE_CALLED;
        return BaseSavedState.EMPTY_STATE;
    }

如果这个 View 是个 ViewGroup 呢，ViewGroup 重写了 dispatchSaveInstanceState 方法，并且调用了super.dispatchSaveInstanceState() 方法，也就是View.dispatchSaveInstanceState()。　

    protected void dispatchSaveInstanceState(SparseArray<Parcelable> container) {
        super.dispatchSaveInstanceState(container);
        final int count = mChildrenCount;
        final View[] children = mChildren;
        for (int i = 0; i < count; i++) {
            View c = children[i];
            if ((c.mViewFlags & PARENT_SAVE_DISABLED_MASK) != PARENT_SAVE_DISABLED) {
                c.dispatchSaveInstanceState(container);
            }
        }
    }

经过上面的代码跟踪，咱们大概知道了在 Activity 的 onSaveInstanceState() 方法被调用的时候，系统都干了些啥事情。相应的，在 onRestoreInstanceState() 的时候，系统又干了些啥，onCreate() 的时候，系统又干了些啥，咱可以按照相同的方法去追踪下去。

不过工作量有点大，我实在看不下去了，哪天有空再说吧……