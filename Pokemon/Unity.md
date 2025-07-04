## 程序部分
start函数
update函数
### input monitor
#### Getkey
#### GetButton
### sprite 处理
TODO sprite 的pivot调整和rotation
#### center of object match 
### timer 时间控制
### Fix endless jump
#### gizmo
Gizmo是Unity编辑器中用于可视化和调试的辅助工具，它允许开发者在Scene视图中绘制简单的几何形状、图标、文本和其他图形元素。Gizmos的主要作用包括：

可视化：Gizmos可以帮助开发者在Scene视图中直观地看到游戏对象的位置、方向和尺寸，这对于调试和调整游戏对象的布局非常有用。

调试：开发者可以使用Gizmos来绘制射线、线段、球体等，以检查物理射线检测、碰撞检测等逻辑是否按预期工作。

辅助设计：在设计游戏场景时，Gizmos可以用来标记关键位置，如敌人的巡逻路径、摄像机的视野范围等。

性能优化：通过Gizmos，开发者可以快速识别和调整那些可能影响性能的游戏对象，如不必要的渲染对象或过多的碰撞体。

教育和演示：在教学或演示中，Gizmos可以用来解释游戏机制，如力的作用、光线传播等。

自定义编辑器工具：开发者可以创建自定义的Gizmos来增强Unity编辑器的功能，使其更适合自己的开发流程。
### finite state machine
在C#中创建有限状态机

解决stateMachine 中的套娃行为 

playerState中需要包含什么成员？
如何进行State的转换？
player  
包含一个  statemachine 来管理状态

而状态变化的条件我应该写在什么位置？
状态变化的条件应该写于状态机中，而不是写在状态中。状态机负责管理状态的转换，而状态的转换条件则由状态机根据当前状态和输入来决定。在状态机中，你可以定义一个方法来处理状态转换，例如：

我需要一个什么样的状态机 一个状态可以切换到多个不同的状态吧应该是？

1.任意时刻只能存在一个状态
2.状态之间可以相互转换 且有不同分支
3.影响状态转换的因素 input；各种参数的变化-speed transition HP etc

core:游戏的核心是需要MonoBehavior 的update()函数 任意input 或者object 状态的检测都需要update()的支持
自然，statemachine状态的转换也需要update()函数

state 分为可打断 和不可打断
interrupt :idle move 
uninterrupt: atk jump  
每个状态都有一个entery condition 除非它处于defult/idle 状态

animator中的animation与status 差不多是一一对应
而animator中的状态转换利用可视化condition来设置

```csharp
public class Entity : MonoBehaviour
{
    protected StateMachine stateMachine;
    protected int HP;
    protected int atk;
    protected int speed;

    private void Start()
    {
        stateMachine.Initialize(idle);
    }
    private void Update()
    {
        stateMachine.checkChange();
    }
}


class StateMachine{
    State currentState;


    Initialize(){

    }
    public void checkChange(){
        currentState.next
    }

}


class State{
    Entity entity;

    protected float moveSpeed;
    protected string animBoolName;

    State():(_entity,_moveSpeed,_animBoolName){}

    public void Enter(){
        //change some attribution
        entity.anim.SetBool(animBoolName,true);
    }
    public void In(){
        
    }
    Public void Exit(){
        // change some attribution
        entity.anim.SetBool(animBoolName,false);
        entity.statemachine.ChangeState();
    }

}

```
## 地图制作
### layer
### background
平行背景

#### endless  bg 
通过平移背景实现
## cinematic studio & camera 重要
1. 让相机跟随人物移动 body改为framing transposer aim  do nothing  player follow
2. dumping 减缓移动
3. lookahead time and smooth
4. 设置deadzone
5. 设置softzone

## Audio manager
管理音效和BGM
### checkDuplicate
### checkDIstance
### 进阶 set a audio UI

### add HP bar and fix flip
#### event
```C#
    //add system event
    public System.Action onFlip;
```
在Unity中，使用 `System.Action` 来定义事件是一种常见的做法。下面是如何添加和使用 `onFlip` 事件的示例，包括如何触发事件和订阅事件的步骤。

#### 1. 定义事件

首先，在你的类中定义 `onFlip` 事件。你可以在类的顶部或构造函数中进行定义：

```csharp
using UnityEngine;

public class FlipHandler : MonoBehaviour
{
    // 定义事件
    public System.Action onFlip;

    // 其他成员变量和方法
}
```

#### 2. 触发事件

在适当的地方（例如，当对象翻转时），你可以调用这个事件。确保在调用之前检查事件是否为 `null`，以避免空引用异常：

```csharp
public void Flip()
{
    // 进行翻转操作
    // ...

    // 触发事件
    onFlip?.Invoke();
}
```

#### 3. 订阅事件

在其他类中，你可以订阅 `onFlip` 事件，以便在事件被触发时执行特定的操作。以下是一个例子：

```csharp
public class EventSubscriber : MonoBehaviour
{
    public FlipHandler flipHandler;

    private void Start()
    {
        // 订阅事件
        if (flipHandler != null)
        {
            flipHandler.onFlip += HandleFlip;
        }
    }

    private void HandleFlip()
    {
        // 处理翻转事件
        Debug.Log("对象已翻转！");
    }

    private void OnDestroy()
    {
        // 取消订阅事件以避免内存泄漏
        if (flipHandler != null)
        {
            flipHandler.onFlip -= HandleFlip;
        }
    }
}
```

#### 4. 使用示例

在Unity编辑器中，将 `FlipHandler` 和 `EventSubscriber` 组件添加到不同的GameObject上，并在 `EventSubscriber` 中引用 `FlipHandler` 的实例。然后，当你调用 `FlipHandler` 中的 `Flip()` 方法时，`EventSubscriber` 中的 `HandleFlip()` 方法将被调用。
 

