from users.models import User

from boards.models import Board
from django.test import TestCase

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user01', password='qwer1234!')
        self.post = Board.objects.create(title='title1',contents='contents1',writer=self.user)

    def test_post_model_create(self):
        board = Board()
        board.title = 'title2'
        board.contents = 'contents'
        board.writer = self.user
        board.save()

        board = Board.objects.get(title='title2')
        self.assertEqual(board.title, 'title2')

    def test_post_model_read(self):
        board = Board.objects.get(id=1)
        self.assertEqual(board.title, 'title1')
    def test_board_model_update(self):
        # 조회하고 바꾸고, 다시 조회했을 때 바뀐 내용으로 바꿔져있어야 함
        board = Board.objects.get(id=1)
        board.title = 'title3'
        board.save()

        board = Board.objects.get(id=1)
        self.assertEqual(board.title, 'title3')
    def test_board_model_delete(self):
        board = Board.objects.get(id=1)
        board.delete()
        self.assertFalse(Board.objects.filter(id=1).exists())
    