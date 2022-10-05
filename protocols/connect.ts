/**
 * 服务器 -> 新加入的玩家
 * 当玩家连接服务器，服务器返回的第一个响应
 */
type connect = {
    type: 'connect',
    value: {
        id: string,         // 服务器分配的 id
        host: boolean       // 是否为房主
    }
}