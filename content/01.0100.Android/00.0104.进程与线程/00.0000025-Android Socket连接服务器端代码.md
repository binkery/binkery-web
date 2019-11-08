# Android Socket连接服务器端代码
- Android,socket,代码,

之前面试的时候遇到一个面试官，让我实现整个socket连接的客户端和服务器端的开发。


需求很简单，读取 Android 客户端通讯录，并上传到服务器端保存，整个流程跑通了就算OK了。基本的东西很少，一个是读取Android 客户端通讯录，一个是客户端的 Socket 连接和超时处理，一个是服务器端的对应功能。

下面是服务器的代码。只大体实现了功能，服务器端可同时与多个客户端进行连接，但是我没有进一步做处理，这个得根据需求另外设计了。接收到的数据我也只是简单的打印出来，没有做保存等处理。

这部分是 JAVA 代码。

    package com.binkery;
    
    import java.io.DataInputStream;
    import java.io.DataOutputStream;
    import java.net.ServerSocket;
    import java.net.Socket;
    import java.util.ArrayList;
    
    public class SocketServer extends Thread{
    
    	private ServerSocket  serverSocker;
    	private static final int PORT = 9527;
    
    	private ArrayList&lt;ClientThread&gt; list = new ArrayList&lt;ClientThread&gt;();
    
    	public SocketServer(){
    		try{
    			serverSocker = new ServerSocket(PORT);
    			System.out.println("开始监听端口 " + PORT);
    		}catch(Exception e){
    			e.printStackTrace();
    		}
    	}
    
    	public void run(){
    		while(true){
    
    			try{
    				Socket socket = serverSocker.accept();
    				System.out.println("监听到一个连接。" + list.size());
    				ClientThread ct = new ClientThread(socket);
    				list.add(ct);
    				ct.start();
    			}catch(Exception e){
    				e.printStackTrace();
    			}
    		}
    	}
    
    	class ClientThread extends Thread{
    		private Socket socket;
    
    		public ClientThread(Socket socket){
    			this.socket = socket;
    		}
    
    		public void run(){
    			try{
    				DataInputStream dis = new DataInputStream(socket.getInputStream());
    				DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
    				System.out.println("IO流建立成功。");
    				int type = dis.readInt();
    				System.out.println("请求类型： " + type);
    				//接收客户端通讯录
    				if(type == 1){
    					String str = dis.readUTF();
    					System.out.println("接收到的数据：" + str);
    					//sleep模拟阻塞
    //					Thread.sleep(5000);
    					System.out.println("开始应答。");
    					dos.write("OK!".getBytes("utf-8"));
    //					Thread.sleep(5000);
    					dos.flush();
    					System.out.println("应答结束。");
    				}else if(type == 2){
    					//待扩展，可做通讯录还原等类似功能用。
    				}
    				dis.close();
    				dos.close();
    				System.out.println("关闭IO完成");
    			}catch(Exception e){
    				e.printStackTrace();
    			}finally{
    				try{
    					socket.close();
    				}catch(Exception e){
    					e.printStackTrace();
    				}
    				socket = null;
    				System.out.println("关闭socket。");
    				boolean isremoved = list.remove(this);
    				System.out.println("是否从队列里移除： " + isremoved);
    				System.out.println("本次请求完成。================");
    			}
    		}
    	}
    
    	public static void main(String[] args){
    		new SocketServer().start();
    	}
    }
