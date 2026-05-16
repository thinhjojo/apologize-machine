#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Multi-language Absurd Apology Generator"""

import random

LANG = {
    'vi': {
        'title': '🎪 MÁY TẠO LỜI XIN LỖI NGỚ NGẪN 🎪',
        'intro': 'Bạn đã quên sinh nhật/kỷ niệm/buổi hẹn? Máy này sẽ tạo lời xin lỗi cho bạn!',
        'prompt': 'Nhấn ENTER để tạo (Ctrl+C để thoát): ',
        'reason_label': 'LÝ DO',
        'action_label': 'HÀNH ĐỘNG',
        'promise_label': 'LẦN SAU',
        'consequence_label': 'THỀ NẾU',
    },
    'en': {
        'title': '🎪 ABSURD APOLOGY GENERATOR 🎪',
        'intro': 'Forgot a birthday/anniversary/date? This machine will create an apology for you!',
        'prompt': 'Press ENTER to generate (Ctrl+C to exit): ',
        'reason_label': 'REASON',
        'action_label': 'ACTION',
        'promise_label': 'NEXT TIME',
        'consequence_label': 'SWORN CONSEQUENCE',
    },
    'zh': {
        'title': '🎪 荒谬道歉生成器 🎪',
        'intro': '忘记了生日/纪念日/约会？这款机器会为你生成道歉！',
        'prompt': '按回车键生成（Ctrl+C退出）：',
        'reason_label': '理由',
        'action_label': '行动',
        'promise_label': '下次',
        'consequence_label': '誓言后果',
    },
    'ja': {
        'title': '🎪 アブсурд お詫びジェネレーター 🎪',
        'intro': '誕生日/記念日/デートのことを忘れましたか？この 기계が謝罪文を生成します！',
        'prompt': 'Enterキーで生成（Ctrl+Cで終了）：',
        'reason_label': '理由',
        'action_label': '行動',
        'promise_label': '次回',
        'consequence_label': '誓いの結果',
    }
}

DATA = {
    'vi': {
        'apology': [
            "Xin lỗi", "Rất tiếc", "Mình rất rất xin lỗi",
            "Mình lạy", "Mình đập đầu xuống đất",
            "Mình quỳ lạy", "Mình bái cảm ơn", "Mình sụp đổ",
            "Mình tan nát", "Mình ôm hận", "Mình khóc ròng",
            "Mình xin đất", "Mình nhận tội", "Mình đầu thú",
            "Mình hết muốn sống", "Mình như chết tới nơi rồi"
        ],
        'reason': [
            "con chó nhà hàng xóm nó cắn cáp mạng",
            "mèo mình nó ngồi lên bàn phím 3 tiếng đồng hồ",
            "tivi nhảy quảng cáo đúng lúc mình định nhắn tin",
            "Facebook suggest đúng 1 bài viết siêu thú vị",
            "mình bị người ngoài hành tinh bắt cóc 3 tiếng",
            "Zoom bị lỗi nhưng thật ra mình chỉ không muốn vào",
            "điện thoại tự động cập nhật OS qua đêm",
            "mình lạc vào một chiều không gian khác",
            "thằng bạn nó gửi meme urgent",
            "Windows update restart không hỏi",
            "mình bị ma ám nhập vào lúc đó",
            "Netflix autoplay ngay lúc quan trọng",
            "Discord nó hiện thông báo sai lúc",
            "mình ngất xỉu vì quá mệt mỏi với cuộc đời",
            "dòng lệnh terminal nó treo không rõ lý do",
            "GitHub merge conflict đánh nhau với mình",
            "mình bị Thanos snap mất nửa não",
            "Docker nó build fail đúng lúc deadline",
            "bàn phím mình dính 2 phím cùng lúc",
            "mình bị rối loạn ám báo khi định nhắn tin",
            "laptop bàn phím rơi trúng ly cà phê",
            "mình bị vong hồn lang thang ở khách sạn",
            "điều hòa treo cửa khi mình định ra ngoài",
            "chó mực tấn công bưu điện lúc mình định gửi quà",
            "router nhà mình đi nghỉ phép"
        ],
        'action': [
            "mình đang cố nhảy lò cò về phía bạn",
            "mình đang ôm gối khóc thương sự ngu ngốc của mình",
            "mình đã tự rút 10 que tăm tự trừng phạt bản thân",
            "mình đang bò về phía bạn như một con rùa",
            "mình thề trên đống tiền mình chưa có",
            "mình đã nhảy flashmob một mình trong phòng",
            "mình đang uống nước cam và hứa hẹn nhiều điều",
            "mình đã treo ảnh bạn lên bàn thờ ngày nào cũng thắp hương",
            "mình đang lạy sám hối 108 lạy",
            "mình đã tự đánh vào mặt mình 10 cái",
            "mình đang quỳ gối trong góc phòng tự nhủ",
            "mình đã đọc hết kinh Phật để chuộc lỗi",
            "mình đang ôm bình cứu hỏa khóc nghẹn",
            "mình đã tự nhốt mình trong tủ quần áo",
            "mình đang bơi về phía bạn bằng dáng bơi brazil",
            "mình đã treo đầu xuống đất như cây đu đủ",
            "mình đang bò bằng tốc độ của một con sên",
            "mình đã viết 100 dòng xin lỗi bằng máu",
            "mình đang hôn đất bùn 36 lần",
            "mình đã nhảy dây 1000 cái để chuộc lỗi"
        ],
        'promise': [
            "lần sau mình sẽ nhắc nhở cả thế giới",
            "mình sẽ đặt 10 cái báo thức",
            "mình sẽ viết lời nhắc lên tay bằng bút đặc biệt",
            "mình đã nhờ cún nhắc giúp mình",
            "mình sẽ nhắn tin bạn mỗi ngày, kể cả khi không có gì",
            "mình sẽ ghi âm lời nhắc vào đá",
            "mình sẽ thuê người đến nhắc nhở mình",
            "mình sẽ nhớ bằng cả trái tim, nhưng không chắc lắm",
            "mình sẽ tattoo lời nhắc lên trán",
            "mình sẽ dán post-it khắp nhà",
            "mình sẽ nhờ cả gia đình nhắc giúp",
            "mình sẽ lập spreadsheet theo dõi",
            "mình sẽ đặt nhạc chuông mỗi 5 phút",
            "mình sẽ viết vào tờ tiền để nhìn mỗi ngày",
            "mình sẽ nhờ Alexa nhắc mỗi sáng",
            "mình sẽ biến bạn thành widget trên điện thoại"
        ],
        'consequence': [
            "nếu không nhớ, mình sẽ tặng bạn một con capybara",
            "nếu quên lần nữa, bạn được quyền đánh mình bằng gối",
            "nếu không nhớ, mình sẽ phải hát một bài trước đám đông",
            "nếu quên, mình sẽ public confession trên mạng xã hội",
            "nếu không nhớ, mình sẽ thuê một billboard ghi sinh nhật bạn",
            "nếu quên, mình sẽ phải nhảy cover dance 1 tiếng",
            "nếu không nhớ, mình sẽ tặng bạn cả một nông trại",
            "nếu quên, bạn được quyền đổi nick mình thành \"Hư Ngư\"",
            "nếu không nhớ, mình sẽ phải ăn hết một nồi cơm cay",
            "nếu quên, mình sẽ phải cosplay một nhân vật anime công khai",
            "nếu không nhớ, mình sẽ phải nói một lời thật lòng trên stage",
            "nếu quên, bạn được quyền đổi avatar mình thành ảnh em bé",
            "nếu không nhớ, mình sẽ phải hôn giày của bạn",
            "nếu quên, mình sẽ phải uống 1 lít tương ớt",
            "nếu không nhớ, mình sẽ phải xóa hết history duyệt web"
        ]
    },
    'en': {
        'apology': [
            "Sorry", "My apologies", "I deeply and desperately apologize",
            "I grovel", "I smash my head on the floor",
            "I kneel before you", "I bow infinitely", "I collapse",
            "I am shattered", "I embrace regret", "I weep rivers",
            "I surrender", "I confess", "I turn myself in",
            "I have lost all will to live", "I am as good as dead"
        ],
        'reason': [
            "the neighbor's dog chewed the ethernet cable",
            "my cat sat on the keyboard for 3 hours",
            "the TV autoplayed an ad at the exact moment I was typing",
            "Facebook suggested a super interesting post",
            "I was abducted by aliens for 3 hours",
            "Zoom crashed but honestly I just didn't want to join",
            "my phone auto-updated OS overnight",
            "I fell into a parallel dimension",
            "my friend sent an urgent meme",
            "Windows update restarted without asking",
            "I was possessed by a demon at that moment",
            "Netflix autoplay kicked in at the crucial moment",
            "Discord showed a notification at the worst time",
            "I fainted from exhaustion with life",
            "the terminal command hung for unknown reasons",
            "GitHub merge conflict attacked me",
            "Thanos snapped half my brain away",
            "Docker build failed right at deadline",
            "my keyboard had 2 keys stuck at once",
            "I was astral projecting while trying to text",
            "a coffee cup fell on my laptop keyboard",
            "my soul wandered into a hotel",
            "the AC froze the door when I was about to leave",
            "a giant squid attacked the post office when I was sending a gift",
            "my router decided to take a vacation"
        ],
        'action': [
            "I'm hopping towards you on one leg",
            "I'm hugging a pillow crying over my own stupidity",
            "I pulled 10 toothpicks to self-punish",
            "I'm crawling towards you like a turtle",
            "I swear on money I don't have",
            "I did a one-person flashmob in my room",
            "I'm drinking orange juice and making grand promises",
            "I hung your photo on my altar and light incense daily",
            "I'm prostrating 108 times in repentance",
            "I slapped myself in the face 10 times",
            "I'm kneeling in the corner muttering to myself",
            "I recited the entire Buddhist sutra to atone",
            "I'm hugging a fire extinguisher sobbing",
            "I locked myself in the closet",
            "I'm swimming towards you with the Brazilian crawl",
            "I've hung my head like a fallen papaya tree",
            "I'm crawling at the speed of a snail",
            "I wrote 100 lines of apology in my own blood",
            "I'm bowing to the ground 36 times",
            "I jumped rope 1000 times to atone"
        ],
        'promise': [
            "next time I'll remind the entire world",
            "I'll set 10 alarms",
            "I'll write the reminder on my hand with special ink",
            "I already hired a dog to remind me",
            "I'll text you every day even when I have nothing to say",
            "I'll record the reminder and carve it into stone",
            "I'll hire a person to come remind me",
            "I'll remember with all my heart, but no guarantees",
            "I'll tattoo the reminder on my forehead",
            "I'll paste post-its all over the house",
            "I'll get my whole family to remind me",
            "I'll create a spreadsheet to track everything",
            "I'll set a ringtone every 5 minutes",
            "I'll write on bills so I see them every day",
            "I'll ask Alexa to remind me every morning",
            "I'll turn you into a widget on my phone"
        ],
        'consequence': [
            "if I forget, I'll gift you a capybara",
            "if I forget again, you may hit me with a pillow",
            "if I forget, I'll have to sing a song in front of everyone",
            "if I forget, I'll public confess on social media",
            "if I forget, I'll rent a billboard for your birthday",
            "if I forget, I'll have to do a 1-hour dance cover",
            "if I forget, I'll give you an entire farm",
            "if I forget, you may change my nickname to 'Useless Jerk'",
            "if I forget, I'll have to eat an entire pot of spicy rice",
            "if I forget, I'll have to cosplay an anime character publicly",
            "if I forget, I'll have to say something truly heartfelt on stage",
            "if I forget, you may change my avatar to a baby photo",
            "if I forget, I'll have to kiss your shoes",
            "if I forget, I'll have to drink 1 liter of hot sauce",
            "if I forget, I'll have to delete all my browsing history"
        ]
    },
    'zh': {
        'apology': [
            "对不起", "非常抱歉", "我深深地、绝望地道歉",
            "我跪了", "我把头砸在地上",
            "我在你面前下跪", "我无限鞠躬", "我崩溃了",
            "我心碎了", "我悔恨交加", "我泪流成河",
            "我投降", "我认罪", "我来自首",
            "我失去了活下去的意志", "我形同已死"
        ],
        'reason': [
            "邻居家的狗咬断了网线",
            "我的猫坐在键盘上3个小时",
            "电视正好在我打字时自动播放广告",
            "Facebook推荐了一个超级有趣的文章",
            "我被外星人绑架了3个小时",
            "Zoom崩溃了，但其实我只是不想加入",
            "我的手机半夜自动更新了系统",
            "我掉进了平行空间",
            "朋友发来了紧急表情包",
            "Windows更新没有问我就重启了",
            "那一刻我被恶魔附身了",
            "Netflix在最关键的时刻自动播放了",
            "Discord在最糟糕的时候弹出了通知",
            "我因为对生活的疲惫而晕倒了",
            "终端命令不明原因卡住了",
            "GitHub合并冲突和我作对",
            "Thanos弹指消灭了我一半的脑子",
            "Docker在截止日期前构建失败",
            "我的键盘同时卡住了2个键",
            "我在发短信时灵魂出窍了",
            "咖啡洒在了笔记本电脑键盘上",
            "我的灵魂在酒店里游荡",
            "空调把门冻住了当我正要出门",
            "一只巨型鱿鱼在我寄礼物时袭击了邮局",
            "我的路由器决定去度假了"
        ],
        'action': [
            "我正单脚跳向你",
            "我抱着枕头为自己的愚蠢而哭泣",
            "我拔了10根牙签自我惩罚",
            "我像乌龟一样爬向你",
            "我对我还没有的钱发誓",
            "我在房间里独自跳了一段快闪",
            "我正在喝橙汁并发誓许多承诺",
            "我把你的照片挂在祭坛上每天上香",
            "我在忏悔中叩首108次",
            "我打了自己10个耳光",
            "我跪在角落里自言自语",
            "我背诵了整部佛经来赎罪",
            "我抱着灭火器痛哭",
            "我把自己锁在衣柜里",
            "我正以巴西泳姿游向你",
            "我的头垂得像一棵木瓜树",
            "我以蜗牛的速度爬行",
            "我用血写了100行道歉",
            "我向地面鞠躬36次",
            "我跳了1000次绳来赎罪"
        ],
        'promise': [
            "下次我会提醒整个世界",
            "我会设置10个闹钟",
            "我会用特殊墨水把提醒写在手上",
            "我已经雇了一只狗来提醒我",
            "我会每天都给你发消息，即使没什么事",
            "我会录下提醒并刻在石头上",
            "我会雇一个人来提醒我",
            "我会用心记住，但不保证",
            "我会在额头上刺青提醒",
            "我会把便利贴贴满全屋",
            "我会让全家人来提醒我",
            "我会创建一个表格来追踪一切",
            "我会每5分钟设置一次铃声",
            "我会写在纸币上这样每天都能看到",
            "我会让Alexa每天早上提醒我",
            "我会把你变成手机上的小部件"
        ],
        'consequence': [
            "如果我忘了，我会送你一只水豚",
            "如果我再忘，你可用枕头打我",
            "如果我忘了，我得在所有人面前唱一首歌",
            "如果我忘了，我会在社交媒体上公开忏悔",
            "如果我忘了，我会租一块广告牌庆祝你的生日",
            "如果我忘了，我得跳1小时的舞蹈翻跳",
            "如果我忘了，我会送你整个农场",
            "如果我忘了，你可以把我的昵称改成'废物'",
            "如果我忘了，我得吃完整锅辣米饭",
            "如果我忘了，我得公开Cosplay一个动漫角色",
            "如果我忘了，我得在舞台上说真心话",
            "如果我忘了，你可以把我的头像换成婴儿照",
            "如果我忘了，我得亲吻你的鞋子",
            "如果我忘了，我得喝下1升辣椒酱",
            "如果我忘了，我得删除所有浏览记录"
        ]
    },
    'ja': {
        'apology': [
            "ごめんなさい", "大変申し訳ありません", "深深地、そして绝望的に謝ります",
            "土下座します", "頭を地に叩きつけます",
            "あなたの前で膝をつきます", "無限に頭を下げます", "崩壊しました",
            "私は粉砕されました", "私は後悔を抱きしめます", "私は川のように泣きます",
            "降伏します", "告白します", "自首します",
            "生きる意欲を失いました", "死んだも同然です"
        ],
        'reason': [
            "近所の犬がLANケーブルを噛んだ",
            "私の猫がキーボードの上に3時間座っていた",
            "テレビがちょうど私がタイプしようとした瞬間にCMが流れた",
            "Facebookがすごく面白い投稿を提案してきた",
            "宇宙人に3時間拉致されました",
            "Zoomがクラッシュしましたが、正直参加したくなかっただけです",
            "私の携帯が夜中にシステムを自動更新した",
            "別の次元に落ちてしまった",
            "友達が緊急ミームを送ってきた",
            "Windowsアップデートが聞かずに再起動した",
            "あの瞬間、悪魔に乗り移られた",
            "Netflixが关键时刻に自動再生した",
            "Discordが最も悪い時に通知を出した",
            "人生の疲労で気を失った",
            "ターミナルコマンドが不明な理由で固まった",
            "GitHubのマージコンフリクトが私を攻撃した",
            "サノスが私の脳の半分を弾き飛ばした",
            "Dockerが締切前にビルド失败了",
            "キーボードの2つのキーが同時に詰まった",
            "メッセージを打とうとして魂が遊離した",
            "コーヒーがノートパソコンキーボードにこぼれた",
            "私の魂がホテルをさまよった",
            "エアコンが私が離れようとした時にドアを凍らせた",
            "巨大イカが私がギフトを送ろうとした時に邮局を攻撃した",
            "私のルーターが休假を取ることになった"
        ],
        'action': [
            "片足であなたの方へ飛んでいます",
            "枕を抱えて自分の愚かさで泣いています",
            "10本の爪楊枝を引いて自罰しています",
            "亀のようにあなたの方へはいずる",
            "持っていないお金に誓います",
            "部屋で一人でフラッシュモブを踊った",
            "オレンジジュースを飲みながら多くの約束をしている",
            "あなたの写真を祭壇に掛けて毎日線香を上げた",
            "懺悔で108回土下座している",
            "自分の顔を10回殴った",
            "部屋の隅に膝をついて独り言を言っている",
            "全文の般若経を暗唱して贖罪した",
            "消火器を抱えて泣いている",
            "クローゼットに自分を鍵めた",
            "ブラジルクロールであなたの方へ泳いでいる",
            "頭を木瓜の木のように垂れている",
            "ナメクジ的速度で這っている",
            "血で100行の謝罪文を書いた",
            "地面に36回頭を下げた",
            "贖罪ために縄跳びを1000回跳んだ"
        ],
        'promise': [
            "次回、世界中に reminders を送る",
            "アラームを10個設定する",
            "特別なインクで手にリマインダーを書く",
            "犬を雇って私に reminder させる",
            "なくても毎日あなたにメッセージを送る",
            "リマインダーを録音して石に刻む",
            "リマインダーをしに来る人を雇う",
            "心で覚えるが、保証はない",
            "額にタトゥーとしてリマインダーを刻む",
            "家中にポストイットを貼り付ける",
            "全家中に reminder させる",
            "全てを追跡するスプレッドシートを作る",
            "5分ごとに着信音を設定する",
            "紙幣に書いて毎日見るようにする",
            "Alexaに毎朝 reminder させる",
            "あなたを电话のウィジェットにする"
        ],
        'consequence': [
            "忘れしたら、カピバラを贈ります",
            "また忘れたら、枕で私を叩いていい",
            "忘れしたら、全員の前で歌わなきゃいけない",
            "忘れしたら、SNSで懺悔する",
            "忘れしたら、あなたの誕生日のビルボードをレンタルする",
            "忘れしたら、1時間ダンスカバーを踊らなきゃいけない",
            "忘れしたら、丸ごと农场を贈る",
            "忘れしたら、ニックネームを「無能な馬鹿」に変えていい",
            "忘れしたら、丸ごと鍋の辛いご飯を食べなきゃいけない",
            "忘れしたら、公共の場でアニメキャラクターのコスプレをする",
            "忘れしたら、ステージで心をこめたことを言わなきゃいけない",
            "忘れしたら、アバターを赤ん坊の写真に変えていい",
            "忘れしたら、あなたの靴をキスしなきゃいけない",
            "忘れしたら、1リットルのタバスコを飲まなきゃいけない",
            "忘れしたら、全浏览履歴を削除しなきゃいけない"
        ]
    }
}

def generate(lang='en'):
    d = DATA[lang]
    l = LANG[lang]
    
    apology = random.choice(d['apology'])
    reason = random.choice(d['reason'])
    action = random.choice(d['action'])
    promise = random.choice(d['promise'])
    consequence = random.choice(d['consequence'])
    
    box = f"""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║  {apology}!                                                     ║
║                                                                  ║
║  {l['reason_label']}: {reason}                                  ║
║                                                                  ║
║  {l['action_label']}: {action}                                    ║
║                                                                  ║
║  {l['promise_label']}: {promise}                                ║
║                                                                  ║
║  {l['consequence_label']}: {consequence}                         ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
    return box

def main():
    print("=" * 65)
    print("  🎪 MULTI-LANGUAGE ABSURD APOLOGY GENERATOR 🎪")
    print("=" * 65)
    print()
    print("Select language / Chọn ngôn ngữ / 选择语言 / 言語を選択:")
    print("  1. English 🇺🇸")
    print("  2. Tiếng Việt 🇻🇳")
    print("  3. 中文简体 🇨🇳")
    print("  4. 日本語 🇯🇵")
    print()
    
    choice = input("Enter 1-4 (default 1): ").strip()
    lang_map = {'1': 'en', '2': 'vi', '3': 'zh', '4': 'ja'}
    lang = lang_map.get(choice, 'en')
    
    l = LANG[lang]
    
    print()
    print("=" * 65)
    print(f"  {l['title']}")
    print("=" * 65)
    print()
    print(l['intro'])
    print()
    
    while True:
        input(l['prompt'])
        print()
        print(generate(lang))

if __name__ == "__main__":
    main()