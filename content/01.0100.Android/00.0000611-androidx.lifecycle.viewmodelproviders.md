# Android JetPack ViewModel 源码分析
- Android源码阅读,ViewModel,JetPack,Android源码分析,ViewModel源码分析,ViewModel学习,AAC源码分析,AndroidJetPack,AndroidViewModel,ViewModelProviders.of(),ViewModelProvider.get()
- 2019.05.24

## ViewModel 介绍

下面是 ViewModel 的定义

> The ViewModel class is designed to store and manage UI-related data in a lifecycle conscious way. The ViewModel class allows data to survive configuration changes such as screen rotations.

简单翻译一下，就是 **ViewModel** 被设计用来存储和管理 UI 相关的数据，以一种可以感知生命周期的方式。ViewModel 可以让数据在配置变化的时候存活下来，比如屏幕发生旋转。

所以我们可以把数据交给 **ViewModel** 来管理，而之前我们习惯让 **Activity** 或在 **Fragment** 来管理。

## ViewModel 使用

使用 ViewModel 第一件事就是 **导入依赖** ，这里忽略不提。

有了依赖，我们就可以写自己的 ViewModel 了。新建一个类 **继承** 于 ViewModel 。

    class MainViewModel : ViewModel(){

        val mainData: MutableLiveData

    }

在 Activity 或者 Fragment 中，获得 ViewModel 对象。

    mViewModel = ViewModelProviders.of(this).get(MainViewModel::class.java)

## ViewModel　源码分析

在这里，Activity 或者 Fragment 并没有直接创建 ViewModel 实例。

### ViewModelProviders

**ViewModelProviders** 重载了多个 **of()** 方法，每一个 of() 方法返回一个 **ViewModelProvider** 对象。of() 方法需要的一个 **FragmentActivity** 或者 **Fragment** ，不能是其他对象，这意味着，你需要在 FragmentActivity 或者 Fragment 里获得 ViewModel，而不能在其他地方随意的获得 ViewModel，除非在持有 FragmentActivity 或者 Fragment 的引用的对象。

    package androidx.lifecycle;
    
    public class ViewModelProviders{
    
        // 这里代码省略了 Fragment 部分的实现
        public static ViewModelProvider of(Fragment fragment){ ... }
        public static ViewModelProvider of(Fragment fragment,Factory factory){ ... }
        
        public static ViewModelProvider of(FragmentActivity activity){ 
            of(activity,null);
        }
        
        public static ViewModelProvider of(FragmentActivity activity,Factory factory){ 
            Application application = checkApplication(activity);
            if(factory == null){
                // 创建工厂对象，这个工厂是用来生产 ViewModel 的。
                factory = ViewModelProvider.AndroidViewModelFactory.getInstance(application);
            }
            return new ViewModelProvider(activity.getViewModelStore(),factory);
        }
    
    }

### ViewModelProvider 

**ViewModelProvider** 里封装了一个 **ViewModelStore**,从 ViewModelProvider 里获取 ViewModel 对象，是先从 ViewModelStore 里查询，如果 ViewModelStore 里不存在指定的 ViewModel，在通过 Factory.create() 方法去创建一个新的 ViewModel 对象。


    package androidx.lifecycle;
    
    public class ViewModelProvider{
    
        private final ViewModelStore mViewModelStore;
        
        public ViewModelProvider(ViewModelStoreOwner owner,Factory factory){
            this(owner.getViewModelStore(),factory);
        }
        
        public ViewModelProvider(ViewModelStore store,Factory factory){
            mFactory = factory;
            this.mViewModelStore = store;
        }
        
        private static final String DEFAULT_KEY = 
                "androidx.lifecycle.ViewModelProvider.DefaultKey";
                
        public <T extends ViewModel> T get(Class<T> modelClass){
            String cannonicalName = modelClass.getCannonicalName();
            if(cannonicalName == null){
                throw new IllegalArgumentException(...)
            }
            return get(DEFAULT_KEY +　":" + cannonicalName, modelClass);
        }
        
        public <T extends ViewModel> T get(String key,Class<T> modelClass){
            ViewModel viewModel = mViewModelStore.get(key);
            if(modelClass.isInstance(viewModel)){
                return (T) viewModel;
            }else{
                if(viewModel != null){
                    // TODO: log a warning ??? 他们也没有想好，为什么会跑到这里来???
                }
            }
            viewModel = mFactory.create(modelClass);
            mViewModelStore.put(key,viewModel);
            return (T) viewModel;
        }
        
        public static class AndroidViewModelFactory extends ViewModelProvider.NewInstanceFactory{
        
            public <T extends ViewModel> T create(Class<T> modelClass){
                if(AndroidViewModel.class.isAssignableFrom(modelClass)){
                    try{
                        // 尝试有参构造器，
                        return modelClass.getConstructor(Application.class).newInstance(mApplication);
                    }catch(...){
                        ...
                    }
                }
                return super.create(modelClass);
            }
        }
        
        public static class NewInstanceFactory implements Factory{
            
            public <T extends ViewModel> T create(Class<T> modelClass){
                try{
                    // 尝试无参构造器
                    return modelClass.newInstance();
                }catch(...){
                    ....
                }
            }
        }
    }



### ViewModelStore

**ViewModelStore** 封装了一个 HashMap，主要是在调用 **put()** 方法和 **clear()** 方法移除旧的 ViewModel 的时候，需要调用 **ViewModel.onCleared()** 方法。

    package androidx.lifecycle;
    public class ViewModelStore{
        private final HashMap<String, ViewModel> mMap = new HashMap<>();

        final void put(String key,ViewModel viewModel){
            ViewModel oldViewModel = mMap.put(key,ViewModel);
            if(oldViewModel != null){
                oldViewModel.onCleared();
            }
        }
    
        final ViewModel get(String key){
            return mMap.get(key);
        }
        
        public final void clear(){ ... }
    
    }
    
### FragmentActivity 中对 ViewModelStore 的管理

**FragmentActivity** 实现了 **ViewModelStoreOwner** 接口，并且对一个 **ViewModelStore** 对象进行了封装。

    package androidx.fragment.app;
    
    public class FragmentActivity extends ComponentActivity implements ViewModelStoreOwner, ...{
    
        private ViewModelStore mViewModelStore;
        
        public ViewModelStore getViewModelStore() {
            if (getApplication() == null) {
                throw new IllegalStateException("Your activity is not yet attached to the "
                        + "Application instance. You can't request ViewModel before onCreate call.");
            }
            if (mViewModelStore == null) {
                mViewModelStore = new ViewModelStore();
            }
            return mViewModelStore;
        }

        protected void onCreate(@Nullable Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            NonConfigurationInstances nc =
                (NonConfigurationInstances) getLastNonConfigurationInstance();
            if (nc != null) {
                mViewModelStore = nc.viewModelStore;
            }
            ...
        }
        
        protected void onDestroy(){
            super.onDestroy();
            if(mViewModelStore != null && !isChangingConfigurations()){
                mViewModelStore.clear();
            }
            ...
        }
        
        public final Object onRetainNonConfigurationInstance(){
            ...
            if(fragment == null && mViewModelStore == null && custom == null){
                return null;
            }
            NonConfigurationInstances nci = new NonConfigurationInstances();
            ...
            nci.viewModelStore = mViewModelStore;
            ...
            return nci;
        }    
    }
    
### ComponentActivity

    public class ComponentActivity extends Activity
        implements LifecycleOwner, KeyEventDispatcher.Component {

        private LifecycleRegistry mLifecycleRegistry = new LifecycleRegistry(this);

        protected void onCreate(@Nullable Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            ReportFragment.injectIfNeededIn(this);
        }

        @Override
        public Lifecycle getLifecycle() {
            return mLifecycleRegistry;
        }
    }


## LifecycleOwner 

**FragmentActivity** 继承于 **ComponentActivity** ， ComponentActivity 现实了 **LifecycleOwner** 接口，LifecycleOwner 接口定义了 getLifecycle() 方法，返回 Lifecycle 。ComponentActivity 实现了 getLifecycle() 方法，返回一个 LifecycleRegistry 对象，LifecycleRegistry 是 Lifecycle 的子类， LifecycleRegistry 有一个 handleLifecycleEvent(@NonNull Lifecycle.Event event) 方法。


    package androidx.lifecycle;

    public interface LifecycleOwner{
        Lifecycle getLifecycle();
    }
    
    
    package androidx.core.app;

    public ComponentActivity extends Activity implements LifecycleOwner{
    
        private LifecycleRegistry mLifecycleRegistry = new LifecycleRegistry(this);

        @Override
        public Lifecycle getLifecycle(){
            return mLifecycleRegistry;
        }
    }
    
    package androidx.lifecycle;
    
    public abstract class Lifecycle{
        
        public abstract void addObserver(LifecycleObserver observer);
        
        public abstract void removeObserver(LifecycleObserver observer);
   
    }
    
    package androidx.lifecycle;
    
    public class LifecycleRegistry extends Lifecycle{
    
        private final WeakReference<LifecycleOwner> mLifecycleOwner;
    
        public LifecycleRegistry(LifecycleOwner provider){
            mLifecycleOwner = new WeakReference<>(provider);
        }
        
        public void addObserver(LifecycleObserver observer){
            State initialState = mState == DESTROYED ? DESTROYED : INITIALIZED;
            ObserverWithState statefulObserver = new ObserverWithState(observer, initialState);
            ObserverWithState previous = mObserverMap.putIfAbsent(observer, statefulObserver);

            if (previous != null) {
                return;
            }
            LifecycleOwner lifecycleOwner = mLifecycleOwner.get();
            if (lifecycleOwner == null) {
                // it is null we should be destroyed. Fallback quickly
                return;
            }

            boolean isReentrance = mAddingObserverCounter != 0 || mHandlingEvent;
            State targetState = calculateTargetState(observer);
            mAddingObserverCounter++;
            while ((statefulObserver.mState.compareTo(targetState) < 0
                    && mObserverMap.contains(observer))) {
                pushParentState(statefulObserver.mState);
                statefulObserver.dispatchEvent(lifecycleOwner, upEvent(statefulObserver.mState));
                popParentState();
                // mState / subling may have been changed recalculate
                targetState = calculateTargetState(observer);
            }

            if (!isReentrance) {
                // we do sync only on the top level.
                sync();
            }
            mAddingObserverCounter--;
        }
    }

## LiveData 

mViewModel.getItemList() 方法返回一个 LiveData 对象，LiveData.observe() 方法传递一个 LifecycleOwner 对象和一个 Observer 对象。

## Lifecycle

Lifecycle 是一个抽象类，主要有三个方法和两个枚举类

    // 添加 Observer
    public abstract void addObserver(@NonNull LifecycleObserver observer);
    // 移除 Observer
    public abstract void removeObserver(@NonNull LifecycleObserver observer);
    // 获取当前状态
    public abstract State getCurrentState();

两个枚举，一个 Event 枚举，代表事件，ON\_CREATE、ON\_START、ON\_RESUME、ON\_PAUSE、ON\_STOP、ON\_DESTROY 和 ON\_ANY 。另外一个枚举 State 代表状态 DESTROYED、INITIALIZED、CREATED、STARTED、RESUMED


## LifecycleRegistry

    public class LifecycleRegistry extends Lifecycle {

        private final WeakReference<LifecycleOwner> mLifecycleOwner;

        public LifecycleRegistry(@NonNull LifecycleOwner provider) {
            mLifecycleOwner = new WeakReference<>(provider);
            mState = INITIALIZED;
        }

        public void handleLifecycleEvent(@NonNull Lifecycle.Event event) {
            State next = getStateAfter(event);
            moveToState(next);
        }


## ReportFragment

ReportFragment 继承于 Fragment ，有一个静态方法 public static void injectIfNeededIn(Activity activity) ,ComponentActivity 的 oncreate() 方法调用了 ReportFragment.injectIfNeededIn(Activity activity)。在 ReportFragment 的生命周期方法会调用 dispatch(Lifecycle.Event event)


    public static void injectIfNeededIn(Activity activity) {
        // ProcessLifecycleOwner should always correctly work and some activities may not extend
        // FragmentActivity from support lib, so we use framework fragments for activities
        android.app.FragmentManager manager = activity.getFragmentManager();
        if (manager.findFragmentByTag(REPORT_FRAGMENT_TAG) == null) {
            manager.beginTransaction().add(new ReportFragment(), REPORT_FRAGMENT_TAG).commit();
            // Hopefully, we are the first to make a transaction.
            manager.executePendingTransactions();
        }
    }


    private void dispatch(Lifecycle.Event event) {
        Activity activity = getActivity();
        if (activity instanceof LifecycleRegistryOwner) {
            ((LifecycleRegistryOwner) activity).getLifecycle().handleLifecycleEvent(event);
            return;
        }

        if (activity instanceof LifecycleOwner) {
            Lifecycle lifecycle = ((LifecycleOwner) activity).getLifecycle();
            if (lifecycle instanceof LifecycleRegistry) {
                ((LifecycleRegistry) lifecycle).handleLifecycleEvent(event);
            }
        }
    }




