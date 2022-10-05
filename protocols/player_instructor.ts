/***
 * 指令发出者 -> 服务器 => 所有玩家
 * 非房主玩家通过键盘发出指令，服务器向其他所有玩家广播该信息
 */
type player_instructor = {
    type: 'player_instructor',
    value: {
        id: string,
        direction:
            'w'  | 'a'  | 's'  | 'd' |
            'wa' | 'wd' | 'sa' | 'sd' | 'space'
    }
}