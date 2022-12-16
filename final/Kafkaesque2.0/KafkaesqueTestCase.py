
# Does not work 
import unittest
import unittest.mock
import io
import Kafkaesque

class KafkaesqueTest(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test1(self,mock_stdout):
        # sig=5
        clerk=[1,23,18,13,99]
        check=0
        total=1
        Kafkaesque.answer(clerk,check,total)
        self.assertEqual(Kafkaesque.test(clerk,check,total),3 )

        
if __name__ == "__main__":
    unittest.main(verbosity = 2)