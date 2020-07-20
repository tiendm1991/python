import java.util.Scanner;
import java.util.TreeSet;

public class Cses {
    static class Ticket implements Comparable {
        int price;
        int idx;

        public Ticket(int price, int idx) {
            this.price = price;
            this.idx = idx;
        }

        public int getPrice() {
            return price;
        }

        public void setPrice(int price) {
            this.price = price;
        }

        public int getIdx() {
            return idx;
        }

        public void setIdx(int idx) {
            this.idx = idx;
        }

        @Override
        public int compareTo(Object o) {
            if (this.getPrice() - ((Ticket) o).getPrice() != 0) {
                return this.getPrice() - ((Ticket) o).getPrice();
            }
            return ((Ticket) o).getIdx() - this.getIdx();
        }

        @Override
        public String toString() {
            return this.getPrice() + "-" + this.getIdx();
        }
    }

    static int n, m;
    static TreeSet<Ticket> h = new TreeSet<Ticket>();

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        m = input.nextInt();
        for (int i = 0; i < n; i++) {
            int x = input.nextInt();
            h.add(new Ticket(x, i));
        }
        for (int i = 0; i < m; i++) {
            int val = input.nextInt();
            Ticket s = h.floor(new Ticket(val, 0));
            if (s != null) {
                System.out.println(s.getPrice());
                h.remove(s);
            } else {
                System.out.println(-1);
            }
        }
    }
}
