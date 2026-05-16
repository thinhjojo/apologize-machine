#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Multi-language Absurd Apology Generator - Fun Edition"""

import random

LANG = {
    'vi': {
        'title': '🎪 MÁY TẠO LỜI XIN LỖI HÀI HƯỚC 🎪',
        'intro': 'Quên sinh nhật/kỷ niệm/buổi hẹn? Đừng lo! Máy này sẽ tạo lời xin lỗi vui nhất cho bạn!',
        'prompt': 'Nhấn ENTER để tạo (Ctrl+C để thoát): ',
        'reason_label': 'LÝ DO',
        'action_label': 'HÀNH ĐỘNG',
        'promise_label': 'LẦN SAU',
        'consequence_label': 'THỀ NẾU',
    },
    'en': {
        'title': '🎪 FUN APOLOGY GENERATOR 🎪',
        'intro': 'Forgot a birthday/anniversary/date? This machine will create the FUNNIEST apology for you!',
        'prompt': 'Press ENTER to generate (Ctrl+C to exit): ',
        'reason_label': 'REASON',
        'action_label': 'ACTION',
        'promise_label': 'NEXT TIME',
        'consequence_label': 'SWORN CONSEQUENCE',
    },
    'zh': {
        'title': '🎪 搞笑道歉生成器 🎪',
        'intro': '忘记了生日/纪念日/约会？这款机器会为你生成最搞笑的道歉！',
        'prompt': '按回车键生成（Ctrl+C退出）：',
        'reason_label': '理由',
        'action_label': '行动',
        'promise_label': '下次',
        'consequence_label': '誓言后果',
    },
    'ja': {
        'title': '🎪 お笑い謝罪ジェネレーター 🎪',
        'intro': '誕生日/記念日/デートのことを忘れましたか？この 기계が、一番面白い謝罪文を生成します！',
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
            "Xin lỗi nha!", "Ơ hay!", "Hề hề!", "Bíp bíp!", 
            "Ting ting!", "Oops!", "Hắc xì!", "Âu dô!",
            "Lạy bạn!", "Kính bạn!", "Hello!", "Hế hế hế!",
            "Bùm bùm!", "Plop plop!", "Tít tắp!", "Hip hip!"
        ],
        'reason': [
            "con chó nhà hàng xóm nó cắn cáp mạng",
            "mèo mình nó ngồi lên bàn phím 3 tiếng đồng hồ",
            "tivi nhảy quảng cáo đúng lúc mình định nhắn tin",
            "Facebook suggest đúng 1 bài viết siêu thú vị",
            "thằng bạn nó gửi meme urgent",
            "Windows update restart không hỏi",
            "Netflix autoplay ngay lúc quan trọng",
            "Discord nó hiện thông báo sai lúc",
            "mình bị lag vì mở quá nhiều tab Chrome",
            "dòng lệnh terminal nó treo không rõ lý do",
            "GitHub merge conflict đánh nhau với mình",
            "Docker nó build fail đúng lúc deadline",
            "bàn phím mình dính 2 phím cùng lúc",
            "laptop bàn phím rơi trúng ly cà phê",
            "điều hòa treo cửa khi mình định ra ngoài",
            "chó mực tấn công bưu điện lúc mình định gửi quà",
            "router nhà mình đi nghỉ phép",
            "mình lười đến nỗi không nhấc điện thoại lên được",
            "pin điện thoại hết đúng lúc mình định gọi",
            "pizza đến đúng lúc mình định nhắn tin",
            "Wifi nhà hàng xóm mạnh hơn nhà mình",
            "mình bị cuốn vào vòng xoáy của một video YouTube",
            "samsung galaxy update lúc 3h sáng",
            "clippy hiện lên hỏi cần giúp gì không",
            "auto-correct đổi tên bạn thành tên một nhân vật anime"
        ],
        'action': [
            "mình đang nhảy moonwalk về phía bạn",
            "mình đang hát rap xin lỗi bạn",
            "mình đã tặng bạn một bức tranh kẻ mắt chó",
            "mình đang làm toast với bơ và mứt cho bạn",
            "mình đã nấu một nồi mì tôm và mang đến cho bạn",
            "mình đang đội nón phi hành gia nói xin lỗi",
            "mình đã vẽ một bức chân dung đẹp nhất của bạn",
            "mình đang làm pizza bay đến nhà bạn",
            "mình đã nhảy ballet một mình trên sân thượng",
            "mình đang đọc thơ xin lỗi bằng giọng opera",
            "mình đã làm một chiếc drone chở hoa đến cho bạn",
            "mình đang trồng một cái cây mang tên bạn",
            "mình đã viết một bài hát về sự ngốc nghếch của mình",
            "mình đang làm yoga cân bằng trên một chân",
            "mình đã làm một con robot nói xin lỗi thay mình",
            "mình đang kể chuyện cười để xin lỗi bạn",
            "mình đã làm một video dance cover xin lỗi",
            "mình đang khiêu vũ với một cây nấm",
            "mình đã kết nối wifi để gửi lời xin lỗi nhanh hơn",
            "mình đang làm một cái máy tính bỏ túi nói xin lỗi"
        ],
        'promise': [
            "lần sau mình sẽ nhắc nhở cả thế giới",
            "mình sẽ đặt 10 cái báo thức",
            "mình sẽ viết lời nhắc lên tay bằng bút đặc biệt",
            "mình đã nhờ cún nhắc giúp mình",
            "mình sẽ nhắn tin bạn mỗi ngày, kể cả khi không có gì",
            "mình sẽ gửi bạn một con vẹt nhắc nhở",
            "mình sẽ thuê người đến nhắc nhở mình",
            "mình sẽ nhớ bằng cả trái tim, có thể lắm",
            "mình sẽ tattoo lời nhắc lên trán bằng henna",
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
            "Oops!", "Whoops!", "Woopsie!", "Surprise!",
            "Ta-da!", "Behold!", "Eureka!", "Ta-daaa!",
            "My bad!", "Oopsie daisy!", "Woopsie poopsie!", "Pardon!",
            "Excuse me!", "Pardon my French!", "Oops a daisy!", "There it is!"
        ],
        'reason': [
            "the neighbor's dog chewed the ethernet cable",
            "my cat sat on the keyboard for 3 hours",
            "the TV autoplayed an ad at the exact moment I was typing",
            "Facebook suggested a super interesting post",
            "my friend sent an urgent meme",
            "Windows update restarted without asking",
            "Netflix autoplay kicked in at the crucial moment",
            "Discord showed a notification at the worst time",
            "I was lagging because I had too many Chrome tabs open",
            "the terminal command hung for unknown reasons",
            "GitHub merge conflict attacked me",
            "Docker build failed right at deadline",
            "my keyboard had 2 keys stuck at once",
            "a coffee cup fell on my laptop keyboard",
            "the AC froze the door when I was about to leave",
            "a giant squid attacked the post office when I was sending a gift",
            "my router decided to take a vacation",
            "I was too lazy to even pick up my phone",
            "my phone battery died at the worst moment",
            "pizza arrived right when I was about to text",
            "neighbor's WiFi is stronger than mine",
            "I got sucked into a YouTube video spiral",
            "Samsung update at 3am somehow",
            "Clippy popped up asking if I need help",
            "auto-correct changed your name to an anime character"
        ],
        'action': [
            "I'm moonwalking towards you",
            "I'm rapping an apology song for you",
            "I gifted you a painting of a dog with sad eyes",
            "I'm making toast with butter and jam for you",
            "I cooked a cup of instant noodles and I'm bringing it to you",
            "I'm wearing a space helmet to say sorry",
            "I drew the most beautiful portrait of you",
            "I'm making pizza fly to your house",
            "I did ballet alone on the rooftop",
            "I'm reciting an apology poem in opera voice",
            "I made a drone carrying flowers for you",
            "I'm planting a tree with your name on it",
            "I wrote a song about my own stupidity",
            "I'm doing yoga balancing on one leg",
            "I made a robot that says sorry for me",
            "I'm telling jokes to apologize",
            "I made a dance cover video as an apology",
            "I'm dancing with a mushroom",
            "I connected to WiFi just to send this apology faster",
            "I'm building a pocket calculator that says sorry"
        ],
        'promise': [
            "next time I'll remind the entire world",
            "I'll set 10 alarms",
            "I'll write the reminder on my hand with special ink",
            "I already hired a dog to remind me",
            "I'll text you every day even when I have nothing to say",
            "I'll send you a parrot that reminds you",
            "I'll hire a person to come remind me",
            "I'll remember with all my heart, maybe",
            "I'll tattoo the reminder on my forehead with henna",
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
            "哎呀!", "哎呦!", "哈喽!", "哇哦!",
            "抱歉啦!", "不好意思!", "打扰了!", "请原谅!",
            "哎嘛呀!", "哇啦啦!", "嘻唰唰!", "砰砰!"
        ],
        'reason': [
            "邻居家的狗咬断了网线",
            "我的猫坐在键盘上3个小时",
            "电视正好在我打字时自动播放广告",
            "Facebook推荐了一个超级有趣的文章",
            "朋友发来了紧急表情包",
            "Windows更新没有问我就重启了",
            "Netflix在最关键的时刻自动播放了",
            "Discord在最糟糕的时候弹出了通知",
            "我因为Chrome开了太多标签页而卡住了",
            "终端命令不明原因卡住了",
            "GitHub合并冲突和我作对",
            "Docker在截止日期前构建失败",
            "我的键盘同时卡住了2个键",
            "咖啡洒在了笔记本电脑键盘上",
            "空调把门冻住了当我正要出门",
            "一只巨型鱿鱼在我寄礼物时袭击了邮局",
            "我的路由器决定去度假了",
            "我太懒了连手机都不想拿起来",
            "我的手机电量刚好用完了",
            "披萨在我要发消息的时候到了",
            "邻居的WiFi比我的强",
            "我被卷入了YouTube视频漩涡",
            "三星在凌晨3点更新了系统",
            "回形针助手弹出问我需要帮助吗",
            "自动更正把你的名字改成了一个动漫角色"
        ],
        'action': [
            "我正用太空步走向你",
            "我正在为你说唱道歉歌",
            "我送给你一幅眼睛忧郁的狗的画",
            "我正在为你做黄油果酱吐司",
            "我煮了一碗泡面正要带给你",
            "我戴着太空头盔说抱歉",
            "我画了你的最美丽的肖像画",
            "我正在让披萨飞到你家",
            "我在天台上独自跳芭蕾",
            "我正在用歌剧的声音朗诵道歉诗",
            "我制造了一架载着花送给你的无人机",
            "我正在种一棵刻有你名字的树",
            "我写了一首关于我愚蠢的歌",
            "我正在单腿做瑜伽平衡",
            "我造了一个替我说抱歉的机器人",
            "我正在讲笑话来道歉",
            "我做了一个舞蹈翻跳视频作为道歉",
            "我正在和蘑菇跳舞",
            "我连上WiFi只是为了更快发送这个道歉",
            "我正在制作一个说抱歉的口袋计算器"
        ],
        'promise': [
            "下次我会提醒整个世界",
            "我会设置10个闹钟",
            "我会用特殊墨水把提醒写在手上",
            "我已经雇了一只狗来提醒我",
            "我会每天都给你发消息，即使没什么事",
            "我会送你一只鹦鹉提醒你",
            "我会雇一个人来提醒我",
            "我会用心记住，但不保证",
            "我会在额头上用指甲花刺青提醒",
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
            "あら!", "うっかり!", "おっと!", "あらあら!",
            "ごめんね!", "すみません!", "失礼!", "お許しを!",
            "あれれ!", "わぁ!", "うょうよ!", "ぷぷっ!"
        ],
        'reason': [
            "近所の犬がLANケーブルを噛んだ",
            "私の猫がキーボードの上に3時間座っていた",
            "テレビがちょうど私がタイプしようとした瞬間にCMが流れた",
            "Facebookがすごく面白い投稿を提案してきた",
            "友達が緊急ミームを送ってきた",
            "Windowsアップデートが聞かずに再起動した",
            "Netflixが关键时刻に自動再生した",
            "Discordが最も悪い時に通知を出した",
            "Chromeのタブを開きすぎてLagっていた",
            "ターミナルコマンドが不明な理由で固まった",
            "GitHubのマージコンフリクトが私を攻撃した",
            "Dockerが締切前にビルド失败了",
            "キーボードの2つのキーが同時に詰まった",
            "コーヒーがノートパソコンキーボードにこぼれた",
            "エアコンが私が離れようとした時にドアを凍らせた",
            "巨大イカが私がギフトを送ろうとした時に邮局を攻撃した",
            "私の路由器が休假を取ることになった",
            "私は電話を取るのも面倒でした",
            "私のスマホのバッテリーがその時切れた",
            "ピッツァがメッセージを送ろうとした時に届いた",
            "近所のWiFiの方が強い",
            "YouTube動画の渦に吸い込まれた",
            "サムスンが午前3時にアップデートした",
            "クリッピングスが弹出して助けが必要かと聞いた",
            "自動修正があなたの名前をアニメキャラクターに変えた"
        ],
        'action': [
            "私はあなたへムーンウォークしている",
            "私はあなたのためにお笑いRAP道歉歌を作っている",
            "私はあなたのために哀しい目の犬の絵を赠った",
            "私はあなたのためにバターとジャムトーストを作っている",
            "私はカップ麺を煮てあなたちに持っていっている",
            "私は宇宙ヘルメットを着けてごめんなさいを言っている",
            "私はあなたの最美の肖像画を描いた",
            "私はピッツァをあなたに飛ばしている",
            "私は屋上で一人バレエピンクスを踊った",
            "私はオペラの声で謝罪詩を朗読している",
            "私は花を持ったドローンを作った",
            "私はあなたの名前を刻んだ木を植えている",
            "私は自分の愚かについて歌を作った",
            "私は片足でヨガバランスをしている",
            "私は代わりに謝罪するロボットを作った",
            "私は冗談を言って謝罪している",
            "私はダンスカバー動画を作った",
            "私はキノコと踊っている",
            "私はより速く謝罪するためWiFiに接続した",
            "私はごめんなさいを言うポケット電卓を作っている"
        ],
        'promise': [
            "次回、世界中に reminders を送る",
            "アラームを10個設定する",
            "特別なインクで手にリマインダーを書く",
            "犬を雇って私に reminder させる",
            "なくても毎日あなたにメッセージを送る",
            "あなたにリマインダーを送るオウムを贈る",
            "リマインダーをしに来る人を雇う",
            "心で覚えるが、保証はない",
            "ヘナで額にタトゥーとしてリマインダーを刻む",
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
    print("  🎪 FUN APOLOGY GENERATOR 🎪")
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
