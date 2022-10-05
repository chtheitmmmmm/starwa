/**
 * 玩家加入三秒后，将向所有套接字发送此消息，表示解除玩家的无敌状态
 */

type player_vincible = {
    type: 'player_vincible',
    value: {
        id: string
    }
}