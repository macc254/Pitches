from app.models import Comment,User
from app import db

def setUp(self):
        self.user_Mercy = User(username = 'Mercy',password = 'cherotich1998', email = 'cherotichm23@gmail.com')
        self.new_comment= Comment(pitch_title='Review for movies',pitch_comment='This pitch is the best thing since sliced bread',user = self.user_Mercy )
        
def tearDown(self):
        Comment.query.delete()
        User.query.delete()