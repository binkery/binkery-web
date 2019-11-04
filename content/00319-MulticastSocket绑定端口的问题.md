# MulticastSocket绑定端口的问题
- 2013-10-14 08:12:03
- 
- android,java,udp,协议,组播,

<p>mDNS的Java实现分析</p><p>JmDNS实现了java的mDNS。在使用这个jar包开发Android应用的时候，我存在一个疑问。我使用jmDNS打开了5353这个端口，并且通过这个端口监听或者发送一些信息。那么如果有两外一个应用，它也用这个工具，使用相同的方式，使用相似的服务。那么是不是会有端口号冲突的问题？如果冲突了，这个端口号是怎么处理的？</p><p>不过经过了一番搜索，看源代码，还有请教同事。我现在的理解和之前的理解还是有点差别的。先从Java层去分析一下jmDNS是怎么实现的。</p><p>首先使用java.net提供的MulticastSocket类来创建一个socket。</p><div class="code">MulticastSocket mSocket = new MulticastSocket(5353);</div><p>然后选加入到某一个组群里。这个组群被定义成224.0.0.251，必须是这个。</p><div class="code">mSocket.joinGroup(InetAddress.getByName("224.0.0.251").getHostAddress());</div><p>然后起一个线程，接收数据包。</p><div class="code">DatagramPacket packet = new DatagramPacket(buff,buff.length);<br />mSocket.receive(packet);</div><p>发送我就不说了，收到数据包后解析我也不说了。</p><p>说一下端口冲突的问题。因为使用的是UDP协议，所以MulticastSocket是可以实现多个对象，重复绑定同一个端口的。至少在我目前测试的结果，这样子做是合法的。</p>