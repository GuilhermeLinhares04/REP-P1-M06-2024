import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from collections import deque

# Código inspirado na documentação do deque
dq = deque(maxlen=10)

# Código inspirado na ponderada BurgerTeleop
class TurtleControl(Node):
    def __init__(self):
        super().__init__('turtle_control')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.cmd_vel_ = Twist()

    def move_forward(self, distance):
        self.cmd_vel_.linear.x = 1.0
        self.cmd_vel_.linear.y = 0.0
        self.cmd_vel_.angular.z = 0.0
        self.publisher_.publish(self.cmd_vel_)
        dq.append(distance)
        self.get_logger().info(f"Movendo pra frente {distance} unidades")

    def rotate(self, angle):
        self.cmd_vel_.linear.x = 0.0
        self.cmd_vel_.linear.y = 0.0
        self.cmd_vel_.angular.z = angle
        self.publisher_.publish(self.cmd_vel_)
        dq.append(angle)
        self.get_logger().info(f"Rotacionando {angle} graus")

# Código inspirado na ponderada MovingTurtle
def main(args=None):
    rclpy.init(args=args)
    turtle_control = TurtleControl()

    while True:
        command = input("Digite os comandos (mover, rodar, sair): ")
        if command == "mover":
            distance = float(input("Digite uma distância: "))
            turtle_control.move_forward(distance)
        elif command == "rodar":
            angle = float(input("Digite um ângulo: "))
            turtle_control.rotate(angle)
        elif command == "sair":
            break
        else:
            print("Comando inválido. Tente novamente.")

    turtle_control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()