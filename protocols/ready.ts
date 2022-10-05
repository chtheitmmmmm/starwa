/**
 * 新玩家 -> 服务器
 * 当新客户端接收到服务器的 global 消息，将发送此消息以确认
 */

type ready = {
    type: 'ready'
}