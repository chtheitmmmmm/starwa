/**
 * 服务器 => 所有玩家
 * 玩家加入
 * 当玩家加入，其他在线玩家收到此信息，而该玩家收到global类型的信息
 */
type player_join = {
    type: 'player_join',
    value: {
        id: string,             // 加入玩家的 id
        code: number,
    }
}