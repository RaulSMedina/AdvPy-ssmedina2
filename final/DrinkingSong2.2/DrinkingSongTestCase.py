import unittest
import unittest.mock
import io
import DrinkingSong

class DrinkingSongTest(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test1(self, mock_stdout):
        amount=3
        drink="milk"
        DrinkingSong.main(amount,drink)
        self.assertEqual(mock_stdout.getvalue(), """3 bottles of milk on the wall, 3 bottles of milk.
Take one down, pass it around, 2 bottles of milk on the wall.

2 bottles of milk on the wall, 2 bottles of milk.
Take one down, pass it around, 1 bottle of milk on the wall.

1 bottle of milk on the wall, 1 bottle of milk.
Take it down, pass it around, no more bottles of milk.

""")
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test2(self,mock_stdout):
        amount=5
        drink="Apple Jucie"
        DrinkingSong.main(amount,drink)
        self.assertEqual(mock_stdout.getvalue(), """5 bottles of Apple Jucie on the wall, 5 bottles of Apple Jucie.
Take one down, pass it around, 4 bottles of Apple Jucie on the wall.

4 bottles of Apple Jucie on the wall, 4 bottles of Apple Jucie.
Take one down, pass it around, 3 bottles of Apple Jucie on the wall.

3 bottles of Apple Jucie on the wall, 3 bottles of Apple Jucie.
Take one down, pass it around, 2 bottles of Apple Jucie on the wall.

2 bottles of Apple Jucie on the wall, 2 bottles of Apple Jucie.
Take one down, pass it around, 1 bottle of Apple Jucie on the wall.

1 bottle of Apple Jucie on the wall, 1 bottle of Apple Jucie.
Take it down, pass it around, no more bottles of Apple Jucie.

""")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test3(self,mock_stdout):
        amount=10
        drink="Dr. Pepper"
        DrinkingSong.main(amount,drink)
        self.assertEqual(mock_stdout.getvalue(), """10 bottles of Dr. Pepper on the wall, 10 bottles of Dr. Pepper.
Take one down, pass it around, 9 bottles of Dr. Pepper on the wall.

9 bottles of Dr. Pepper on the wall, 9 bottles of Dr. Pepper.
Take one down, pass it around, 8 bottles of Dr. Pepper on the wall.

8 bottles of Dr. Pepper on the wall, 8 bottles of Dr. Pepper.
Take one down, pass it around, 7 bottles of Dr. Pepper on the wall.

7 bottles of Dr. Pepper on the wall, 7 bottles of Dr. Pepper.
Take one down, pass it around, 6 bottles of Dr. Pepper on the wall.

6 bottles of Dr. Pepper on the wall, 6 bottles of Dr. Pepper.
Take one down, pass it around, 5 bottles of Dr. Pepper on the wall.

5 bottles of Dr. Pepper on the wall, 5 bottles of Dr. Pepper.
Take one down, pass it around, 4 bottles of Dr. Pepper on the wall.

4 bottles of Dr. Pepper on the wall, 4 bottles of Dr. Pepper.
Take one down, pass it around, 3 bottles of Dr. Pepper on the wall.

3 bottles of Dr. Pepper on the wall, 3 bottles of Dr. Pepper.
Take one down, pass it around, 2 bottles of Dr. Pepper on the wall.

2 bottles of Dr. Pepper on the wall, 2 bottles of Dr. Pepper.
Take one down, pass it around, 1 bottle of Dr. Pepper on the wall.

1 bottle of Dr. Pepper on the wall, 1 bottle of Dr. Pepper.
Take it down, pass it around, no more bottles of Dr. Pepper.

""")

if __name__ == "__main__":
    unittest.main(verbosity = 2)

# I used https://realpython.com/python-testing/ as help for the code above