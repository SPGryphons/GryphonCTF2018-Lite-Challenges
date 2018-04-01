using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ConsoleApp1
{
    class Program
    {
        [STAThread]
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("Press any key to exit");
            Clipboard.SetText("GCTF{a_l1ttl3_3x7r4_d1dn7_hur7_n0b0dy}");
            Console.ReadKey();
        }
    }
}