css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn2.iconfinder.com/data/icons/funtime-objects-part-1/60/005_008_robot_baby_friend_gift_present_samodelkin-1024.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn0.iconfinder.com/data/icons/occupation-5-women/504/researcher-assistant-professor-academic-lecturer-1024.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

footer="""<style>
.a-footer {
    position: fixed;
    height: 50px;
    bottom: 0px;
    left: 0px;
    width: 100%;
    background-color: #00000;
    color: grey;
    text-align: right;
    padding: 10px;
}
</style>
<div class='a-footer'>
    <p>made with ❤️ for emily jane by tahsinac</p>
</div>
"""