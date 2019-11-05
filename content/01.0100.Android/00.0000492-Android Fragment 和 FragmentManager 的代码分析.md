# Android Fragment 和 FragmentManager 的代码分析
- 2016-03-22 03:45:45
- 
- 

<!--markdown--># Android Fragment 和 FragmentManager 的代码分析

这两天在研究插件化编程，在使用 Fragment 碰到了一些问题，于是查看源码，顺便分析了一下 Fragment 和 FragmentManager 以及其他几个 API 的原代码，看看他们是怎么工作的。



我们知道 Fragment 有个 onCreateView() 方法，这个方法在 Fragment 创建 View 的时候被调用，并且返回一个 View 对象。那么 onCreateView 在什么时候被调用呢，咱们在 Fragment 这个类里找到了一个方法，performCreateView() 方法。

    Fragment.java
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container,
            @Nullable Bundle savedInstanceState) {
        return null;
    }

performCreateView 这个方法在什么时候会被调用呢，在 Fragment 里找不到调用它的代码。咱们可以猜测一下，大概会在 FragmentManager 里。
	
    View performCreateView(LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState) {
        if (mChildFragmentManager != null) {
            mChildFragmentManager.noteStateNotSaved();
        }
        return onCreateView(inflater, container, savedInstanceState);
    }

在 FragmentManager 里，咱们找到了调用 Fragment.performCreateView 的代码，在 moveToState() 方法里，这个方法有点大，我只粘贴了部分代码。可以看到，它会在 Fragment 初始化或者创建的时候被调用。并且我们知道，创建的View 被赋值给 Fragment 的 mView 成员变量了。

    FragmentManager.java
    void moveToState(Fragment f, int newState, int transit, int transitionStyle, boolean keepActive) {
	
        switch (f.mState) {
        case Fragment.INITIALIZING:
            if (f.mFromLayout) {
                f.mView = f.performCreateView(f.getLayoutInflater(
                f.mSavedFragmentState), null, f.mSavedFragmentState);
	    }
	    break;
	case Fragment.CREATED:
	    if (!f.mFromLayout) {
	        f.mView = f.performCreateView(f.getLayoutInflater(
                f.mSavedFragmentState), container, f.mSavedFragmentState);
	    }
	break;
	}	
    }
	
接下来，咱们要看什么时候会调用 moveToState() 这个方法。找了一下，发现很 N 多的地方调用了这个方法。这样给咱们逆推找代码造成了一定的难度。于是咱们换个思路，正推来分析。怎么正推了，看咱们怎么使用 Fragment 和 FragmentManager 来分析。

一般咱们都是 getFragmentManager() 或者 getSupportFragmentManager() 的方法来获取 FragmentManager.以 FragmentActivity 为例，一般情况下，咱们在这个类的子类里调用这两个方法之一。

咱们在 FragmentActivity 里找到了相应的代码。FragmentManager 是一个抽象类，FragmentManagerImpl 是 FragmentManager 的子类，在 FragmentManager 同一个 java 文件内，是一个内部类。它是 FragmentManager 的实现。
	
    FragmentActivity.java

    //FragmentManagerImpl is subclass of FragmentManager
    final FragmentManagerImpl mFragments = new FragmentManagerImpl();
	
    public FragmentManager getSupportFragmentManager() {
        return mFragments;
    }
	
获取到 FragmentManager 后，咱们一般就会调用 beginTransaction() 方法，返回一个 FragmentTransaction 。咱们看代码去。
	
    FragmentManager.java
    public abstract FragmentTransaction beginTransaction();

    FragmentManagerImpl extends FragmentManager

    @Override
    public FragmentTransaction beginTransaction() {
        return new BackStackRecord(this);
    }
	
    /**
    * Static library support version of the framework's {@link android.app.FragmentTransaction}.
    * Used to write apps that run on platforms prior to Android 3.0.  When running
    * on Android 3.0 or above, this implementation is still used; it does not try
    * to switch to the framework's implementation.  See the framework SDK
    * documentation for a class overview.
    */
    public abstract class FragmentTransaction
	
我们发现 FragmentManager 是一个抽象方法，实现在 FragmentManagerImpl。FragmentManagerImpl.beginTransaction() 返回的是一个BackStackRecord，而 FragmentTransaction 是一个抽象类。那么 BackStackRecord 是个什么鬼。
	
我们找到了 BackStackRecord 这个类。我们注意到，它继承于 FragmentTransaction，并且实现了 Runable 接口。它的方法有很多，咱们就分析一个咱们比较常用的，比如 add() 方法。

    BackStackRecord.java

    final class BackStackRecord extends FragmentTransaction implements FragmentManager.BackStackEntry, Runnable 
    final FragmentManagerImpl mManager;
    public BackStackRecord(FragmentManagerImpl manager) {
        mManager = manager;
    }
	
add() 方法其实没干啥，咱们一路追下去看。
	
    public FragmentTransaction add(Fragment fragment, String tag) {
        doAddOp(0, fragment, tag, OP_ADD);
        return this;
    }
	
    private void doAddOp(int containerViewId, Fragment fragment, String tag, int opcmd) {
        fragment.mFragmentManager = mManager;

        if (tag != null) {
            if (fragment.mTag != null && !tag.equals(fragment.mTag)) {
                throw new IllegalStateException("Can't change tag of fragment "
                        + fragment + ": was " + fragment.mTag
                        + " now " + tag);
            }
            fragment.mTag = tag;
        }

        if (containerViewId != 0) {
            if (fragment.mFragmentId != 0 && fragment.mFragmentId != containerViewId) {
                throw new IllegalStateException("Can't change container ID of fragment "
                        + fragment + ": was " + fragment.mFragmentId
                        + " now " + containerViewId);
            }
            fragment.mContainerId = fragment.mFragmentId = containerViewId;
        }
		
        Op op = new Op();
        op.cmd = opcmd;
        op.fragment = fragment;
        addOp(op);
    }
	
    void addOp(Op op) {
        if (mHead == null) {
            mHead = mTail = op;
        } else {
            op.prev = mTail;
            mTail.next = op;
            mTail = op;
        }
        op.enterAnim = mEnterAnim;
        op.exitAnim = mExitAnim;
        op.popEnterAnim = mPopEnterAnim;
        op.popExitAnim = mPopExitAnim;
        mNumOp++;
    }
	
一直追到 addOp() 就断了，好像啥事也没干。不过它大概是在一个 add 操作添加到一个链表上了。那咱们怎么办呢？一般咱们add 完后会 commit 一下，咱们看看 commit 都干了啥。
	
    public int commit() {
        return commitInternal(false);
    }
	
    int commitInternal(boolean allowStateLoss) {
        if (mCommitted) throw new IllegalStateException("commit already called");

        mCommitted = true;
        if (mAddToBackStack) {
            mIndex = mManager.allocBackStackIndex(this);
        } else {
            mIndex = -1;
        }
        mManager.enqueueAction(this, allowStateLoss);
        return mIndex;
    }
	
commit 好像也没干啥特殊的事情，不过可以看到这么一行代码 mManager.enqueueAction(this, allowStateLoss); 看 enqueueAction 这个方法名，应该会做点事情的。
	
同样，咱们在 FragmentManagerImpl 里找到了这个方法。

FragmentManager.java 	FragmentManagerImpl

    public void enqueueAction(Runnable action, boolean allowStateLoss) {
        if (!allowStateLoss) {
            checkStateLoss();
        }
        synchronized (this) {
            if (mDestroyed || mActivity == null) {
                throw new IllegalStateException("Activity has been destroyed");
            }
            if (mPendingActions == null) {
                mPendingActions = new ArrayList<Runnable>();
            }
            mPendingActions.add(action);
            if (mPendingActions.size() == 1) {
                mActivity.mHandler.removeCallbacks(mExecCommit);
                mActivity.mHandler.post(mExecCommit);
            }
        }
    }
	
这个方法把咱们的 BackStackRecord -- 其实是 FragmentTransaction，也是 Runnable -- 添加到一个 mPendingActions 的 ArrayList 里了。然后调用 mActivity.mHandler.post(mExecCommit); mExecCommit 又是什么鬼？

    Runnable mExecCommit = new Runnable() {
        @Override
        public void run() {
            execPendingActions();
        }
    };
	
mActivity.mHandler.post(mExecCommit); 说明它在主线程里执行了 mExecCommit 的 run 方法。别问我咋知道的。

execPendingActions() 方法稍微比较大，我把注释写在代码里。

	public boolean execPendingActions() {
        if (mExecutingActions) {
            throw new IllegalStateException("Recursive entry to executePendingTransactions");
        }
        //如果不是在主线程，抛出一个异常。
        if (Looper.myLooper() != mActivity.mHandler.getLooper()) {
            throw new IllegalStateException("Must be called from main thread of process");
        }

        boolean didSomething = false;
		// 这里有一个 while true 循环。
        while (true) {
            int numActions;
            // 这里在一个同步语句块里，把上次 mPendingActions 里的元素转移到 mTmpActions 数组里。并且执行 run方法。执行谁的 run 方法呢？！就是 BackStackRecord ， 也就是 FragmentTransaction 。我在最后面贴了 BackStackRecord 的 run 方法。
            synchronized (this) {
                if (mPendingActions == null || mPendingActions.size() == 0) {
                    break;
                }
                
                numActions = mPendingActions.size();
                if (mTmpActions == null || mTmpActions.length < numActions) {
                    mTmpActions = new Runnable[numActions];
                }
                mPendingActions.toArray(mTmpActions);
                mPendingActions.clear();
                mActivity.mHandler.removeCallbacks(mExecCommit);
            }
            
            mExecutingActions = true;
            for (int i=0; i<numActions; i++) {
                mTmpActions[i].run();
                mTmpActions[i] = null;
            }
            mExecutingActions = false;
            didSomething = true;
        }
        // 这里有好几行代码，不知道干啥的，反正就是做了一些判断，最后可能会调用 startPendingDeferredFragments() 方法。
        if (mHavePendingDeferredStart) {
            boolean loadersRunning = false;
            for (int i=0; i<mActive.size(); i++) {
                Fragment f = mActive.get(i);
                if (f != null && f.mLoaderManager != null) {
                    loadersRunning |= f.mLoaderManager.hasRunningLoaders();
                }
            }
            if (!loadersRunning) {
                mHavePendingDeferredStart = false;
                startPendingDeferredFragments();
            }
        }
        return didSomething;
    }
	
startPendingDeferredFragments 方法又是一坨不知道啥意思的代码。最后可能调用了 performPendingDeferredStart() 

    void startPendingDeferredFragments() {
        if (mActive == null) return;

        for (int i=0; i<mActive.size(); i++) {
            Fragment f = mActive.get(i);
            if (f != null) {
                performPendingDeferredStart(f);
            }
        }
    }

在 这个方法里，咱们看到了很熟悉的 moveToState() 方法。接着就是上面的分析，Fragment 的 onCreateView 会被调用。

    public void performPendingDeferredStart(Fragment f) {
        if (f.mDeferStart) {
            if (mExecutingActions) {
                // Wait until we're done executing our pending transactions
                mHavePendingDeferredStart = true;
                return;
            }
            f.mDeferStart = false;
            moveToState(f, mCurState, 0, 0, false);
        }
    }

	咱们在回来看 BackStackRecord 的 run 方法。这坨代码有点大，我还是写注释在代码里。
BackStackRecord.java

    public void run() {
        if (FragmentManagerImpl.DEBUG) Log.v(TAG, "Run: " + this);

        if (mAddToBackStack) {
            if (mIndex < 0) {
                throw new IllegalStateException("addToBackStack() called after commit()");
            }
        }

        bumpBackStackNesting(1);

        TransitionState state = null;
        SparseArray<Fragment> firstOutFragments = null;
        SparseArray<Fragment> lastInFragments = null;
        if (SUPPORTS_TRANSITIONS) {
            firstOutFragments = new SparseArray<Fragment>();
            lastInFragments = new SparseArray<Fragment>();

            calculateFragments(firstOutFragments, lastInFragments);

            state = beginTransition(firstOutFragments, lastInFragments, false);
        }

        int transitionStyle = state != null ? 0 : mTransitionStyle;
        int transition = state != null ? 0 : mTransition;
		// 注意这里要开始 while 循环了，要遍历刚才咱们说的链表了。
        Op op = mHead;
        while (op != null) {
            int enterAnim = state != null ? 0 : op.enterAnim;
            int exitAnim = state != null ? 0 : op.exitAnim;
            switch (op.cmd) {
				// OP_ADD 很简单，mManager.addFragment(f, false); 其他的几个也类似，调用 mManager 相应的方法。
                case OP_ADD: {
                    Fragment f = op.fragment;
                    f.mNextAnim = enterAnim;
                    mManager.addFragment(f, false);
                } break;
                case OP_REPLACE: {
                    Fragment f = op.fragment;
                    if (mManager.mAdded != null) {
                        for (int i=0; i<mManager.mAdded.size(); i++) {
                            Fragment old = mManager.mAdded.get(i);
                            if (FragmentManagerImpl.DEBUG) Log.v(TAG,
                                    "OP_REPLACE: adding=" + f + " old=" + old);
                            if (f == null || old.mContainerId == f.mContainerId) {
                                if (old == f) {
                                    op.fragment = f = null;
                                } else {
                                    if (op.removed == null) {
                                        op.removed = new ArrayList<Fragment>();
                                    }
                                    op.removed.add(old);
                                    old.mNextAnim = exitAnim;
                                    if (mAddToBackStack) {
                                        old.mBackStackNesting += 1;
                                        if (FragmentManagerImpl.DEBUG) Log.v(TAG, "Bump nesting of "
                                                + old + " to " + old.mBackStackNesting);
                                    }
                                    mManager.removeFragment(old, transition, transitionStyle);
                                }
                            }
                        }
                    }
                    if (f != null) {
                        f.mNextAnim = enterAnim;
                        mManager.addFragment(f, false);
                    }
                } break;
                case OP_REMOVE: {
                    Fragment f = op.fragment;
                    f.mNextAnim = exitAnim;
                    mManager.removeFragment(f, transition, transitionStyle);
                } break;
                case OP_HIDE: {
                    Fragment f = op.fragment;
                    f.mNextAnim = exitAnim;
                    mManager.hideFragment(f, transition, transitionStyle);
                } break;
                case OP_SHOW: {
                    Fragment f = op.fragment;
                    f.mNextAnim = enterAnim;
                    mManager.showFragment(f, transition, transitionStyle);
                } break;
                case OP_DETACH: {
                    Fragment f = op.fragment;
                    f.mNextAnim = exitAnim;
                    mManager.detachFragment(f, transition, transitionStyle);
                } break;
                case OP_ATTACH: {
                    Fragment f = op.fragment;
                    f.mNextAnim = enterAnim;
                    mManager.attachFragment(f, transition, transitionStyle);
                } break;
                default: {
                    throw new IllegalArgumentException("Unknown cmd: " + op.cmd);
                }
            }

            op = op.next;
        }
		// 最后还调用了moveToState() 这个方法。跟刚才的区别，看最后一个参数，一个true，一个false。
		// 而且注意，这行代码在 while 循环之后。
        mManager.moveToState(mManager.mCurState, transition, transitionStyle, true);

        if (mAddToBackStack) {
            mManager.addBackStackState(this);
        }
    }

分析得不是很彻底，但是能大概看出 Fragment 是怎么被创建的。以及相对应的几个 API 大概做了些什么。
	