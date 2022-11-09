package mainpkg // potentially unnecessary
import testpkg.TestSuite
    
class General {
    public static void main(String[] args) {
	TestSuite tests = new TestSuite(args[0]);
    }
}
