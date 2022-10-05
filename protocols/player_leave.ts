/**
 * 服务器 => 所有玩家
 * 玩家离开时，服务器向所有玩家广播此条消息
 */
type player_leave = {
    type: 'player_leave',
    value: {
        id: string
    }
}