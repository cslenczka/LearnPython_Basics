# We can use a 2 dimensional array (matrix) to represent the current state of a parking lot
# Create a function get_parking_lot() that returns a dictionary with total_slots, available_slots and occupied_slots like the following:
# state = {
#     total_slots: 12,
#     available_slots: 3,
#     occupied_slots: 9
# }
#💡 Hint: Declare the key names to store the values. You have to do a nested loop. Compare the statements.

parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

def get_parking_lot(parking_state):
    state = {
        "total_slots": 0,
        "available_slots": 0,
        "occupied_slots": 0
    }
    for row in parking_state:
        for slot in row:
            state["total_slots"] += 1
            if slot == 1:
                state["available_slots"] += 1
            elif slot == 2:
                state["occupied_slots"] += 1
    return state

print('state = ' + str(get_parking_lot(parking_state)))

# Expected output:
# {
#     "total_slots": 9,
#     "available_slots": 4,
#     "occupied_slots": 5
# }
#
# Another way to do it using list comprehension example 1:
# Hint: You can use the sum() function to count the number of 1's and 2's in the matrix.
#
# def get_parking_lot(parking_state):
#     state = {
#         "total_slots": 0,
#         "available_slots": 0,
#         "occupied_slots": 0
#     }
#     state["total_slots"] = sum([len(row) for row in parking_state])
#     state["available_slots"] = sum([row.count(1) for row in parking_state])
#     state["occupied_slots"] = sum([row.count(2) for row in parking_state])
#     return state
#
# print(get_parking_lot(parking_state))
#
# # Another way to do it using list comprehension example 2:
# Hint: You can use the sum() function to count the number of 1's and 2's in the matrix.
# def get_parking_lot(parking_state):
#     state = {
#         "total_slots": 0,
#         "available_slots": 0,
#         "occupied_slots": 0
#     }
#     state["total_slots"] = sum([len(row) for row in parking_state])
#     state["available_slots"] = sum([1 for row in parking_state for slot in row if slot == 1])
#     state["occupied_slots"] = sum([1 for row in parking_state for slot in row if slot == 2])
#     return state
#
# print(get_parking_lot(parking_state))