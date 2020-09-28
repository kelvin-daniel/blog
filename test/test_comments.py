import unittest
from app.models import Comment, Blog, User
from app import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        
        self.new_comment = Comment(id = 1, comment = 'i was here', user = self.user_keen, blog_id = self.new_blog)
        
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'i was here')
        self.assertEquals(self.new_comment.user,self.user_keen)
        self.assertEquals(self.new_comment.blog_id,self.new_blog)


class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_billy = User(username='bildad', password='bilmom', email='dad@mom.com')
        self.new_blog = Blog(id=1, title='bilmomdad', content='billy momomo dadada', user_id=self.user_billy.id)
        self.new_comment = Comment(id=1, comment ='i was here', user_id=self.user_billy.id, blog_id = self.new_blog.id )

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment, 'i was here')
        self.assertEquals(self.new_comment.user_id, self.user_billy.id)
        self.assertEquals(self.new_comment.blog_id, self.new_blog.id)

    def test_save_comment(self):
        self.new_comment.save()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_get_comment(self):
        self.new_comment.save()
        got_comment = Comment.get_comment(1)
        self.assertTrue(get_comment is not None)