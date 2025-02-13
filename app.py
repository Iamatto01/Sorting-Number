from flask import Flask, render_template, request
from Iterative import Node, bidirectional_selection_sort_iterative

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    numbers = request.form['numbers']
    number_list = [int(x) for x in numbers.split(',')]
    
    # Create linked list from number_list
    head = Node(number_list[0])
    current = head
    for number in number_list[1:]:
        current.next = Node(number)
        current = current.next
    
    # Sort the linked list
    sorted_head = bidirectional_selection_sort_iterative(head)
    
    # Convert sorted linked list back to Python list
    sorted_list = []
    while sorted_head:
        sorted_list.append(sorted_head.data)
        sorted_head = sorted_head.next
    
    return render_template('sorted.html', sorted_list=sorted_list)

if __name__ == '__main__':
    app.run(debug=True)
