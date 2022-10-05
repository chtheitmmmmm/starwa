/**
 * 房主玩家 -> 服务器 => 所有玩家
 * 怪物运动
 */
type enemy_instructor = {
    type: 'enemy_instructor',
    value: {
        instructor: 'add'             // 添加一个怪物
        id: number,                   // 怪物的id是产生的时间戳
        code: number,
        pos: [number, number]
    } | {
        instructor: 'accelerate'      // 使动一个怪物
        id: string,
        direction:
            'w'  | 'a'  | 's'  | 'd' |
            'wa' | 'wd' | 'sa' | 'sd'
    } | {
        instructor: 'shoot'           // 使怪物执行射击动作
        id: string
    }
}