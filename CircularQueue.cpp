#include <iostream>
using namespace std;

#define SIZE 5

class CircularQueue {
    int q[SIZE], front, rear;

public:
    CircularQueue() {
        front = rear = -1;
    }

    void enqueue(int x) {
        if ((rear + 1) % SIZE == front) {
            cout << "Queue is Full\n";
            return;
        }

        if (front == -1)
            front = 0;

        rear = (rear + 1) % SIZE;
        q[rear] = x;
        cout << x << " inserted\n";
    }

    void dequeue() {
        if (front == -1) {
            cout << "Queue is Empty\n";
            return;
        }

        cout << q[front] << " deleted\n";

        if (front == rear)
            front = rear = -1;
        else
            front = (front + 1) % SIZE;
    }

    void display() {
        if (front == -1) {
            cout << "Queue is Empty\n";
            return;
        }

        int i = front;
        while (true) {
            cout << q[i] << " ";
            if (i == rear) break;
            i = (i + 1) % SIZE;
        }
        cout << endl;
    }
};

int main() {
    CircularQueue cq;
    int ch, x;

    do {
        cout << "\n1.Enqueue  2.Dequeue  3.Display  4.Exit\n";
        cout << "Enter choice: ";
        cin >> ch;

        switch (ch) {
            case 1:
                cout << "Enter element: ";
                cin >> x;
                cq.enqueue(x);
                break;

            case 2:
                cq.dequeue();
                break;

            case 3:
                cq.display();
                break;

            case 4:
                cout << "Exit\n";
                break;

            default:
                cout << "Invalid choice\n";
        }
    } while (ch != 4);

    return 0;
}
