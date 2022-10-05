/**
 * 房主玩家 -> 服务器 -> 新加入的非房主玩家
 * 游戏的全部信息
 * 在服务器发送connect类型的信息后，服务器将向房主玩家请求该信息，
 *  若房主玩家返回该信息，则服务器将其转发给新加入的玩家
 *  否则服务器将考虑另立房主，直到所有其他玩家不可用，服务器将尝试发送类型为 host 的消息给该玩家
 *  玩家刚加入会进入三秒钟的无敌状态
 */

type global = {
    type: 'global',
    value: {
        players: Array<{
            id: string,                // 玩家 id
            code: number,              // 玩家飞机代号
            speed: [number, number]
            accelerate: [number, number]
            pos: [number, number]         // 位置，用二元列表
            hp: number                 // 剩余生命值
        }>
        enemys: Array<{
            id: number,           // 怪物id
            code: number,         // 怪物飞机代号
            speed: [number, number]
            accelerate: [number, number]
            pos: [number, number] // 怪物飞机位置
            hp: number,           // 剩余生命值
        }>
        bgpos: Array<number>    // 背景图片的位置
    }
}