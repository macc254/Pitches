
import unittest
from app.models import Comment,User
from app import db
 
class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Comment class
    '''
    
def setUp(self):
        self.user_Mercy = User(username = 'Mercy',password = 'cherotich1998', email = 'cherotichm23@gmail.com')
        self.new_comment= Comment(pitch_title='Comment for pitches',pitch_comment='This pitch is the best thing since sliced bread',user = self.user_Mercy )
        
def tearDown(self):
        Comment.query.delete()
        User.query.delete()
def test_init(self):
    self.assertEquals(self.new_comment.pitch_title,'Comment for pitches')
    self.assertEquals(self.new_comment.pich_comment,'This pitch is the best thing since sliced bread')
    self.assertEquals(self.new_comment.user,self.user_Mercy)
def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
def test_get_comment(self):

        self.new_comment.save_comment()
        got_comment = Comment.get_comment('Comment for pitches')
        self.assertTrue(len(got_comment) == 1)