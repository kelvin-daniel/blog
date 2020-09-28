import unittest
from app.models import Blog, User,
from app import db


class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_billy = User(username='bildad', password='bilmom', email='dad@mom.com')
        self.new_blog = Blog(id=1, title='bilmomdad', content='billy momomo dadada', user_id=self.user_billy.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'bilmomdad')
        self.assertEquals(self.new_blog.content, 'billy momomo dadada')
        self.assertEquals(self.new_blog.user_id, self.user_charles.id)

    def test_save_blog(self):
        self.new_blog.save()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save()
        got_blog = Blog.get_blog(1)
        self.assertTrue(get_blog is not None)