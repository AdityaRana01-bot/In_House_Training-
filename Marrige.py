{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "787c516c-19dd-4e1f-bc5d-22307aa1bb8c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your age:  23\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You have 2 years left until typical marriage age.\n"
     ]
    }
   ],
   "source": [
    "\n",
    "marriage_age = 25\n",
    "\n",
    "# Take user's age\n",
    "age = int(input(\"Enter your age: \"))\n",
    "\n",
    "# Check and respond\n",
    "if age < marriage_age:\n",
    "    print(\"You have\", marriage_age - age, \"years left until typical marriage age.\")\n",
    "elif age == marriage_age:\n",
    "    print(\"You are at the typical marriage age!\")\n",
    "else:\n",
    "    print(\"You passed the typical marriage age by\", age - marriage_age, \"years.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fc6758bc-ba50-4801-b085-98b0de59ad9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter total water bottles:  4\n",
      "Enter bottles you drink per day:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Day 1: Drank 3 bottles. 1 left.\n",
      "Day 2: Drank 1 bottle. 0 left.\n",
      "No more bottles left!\n"
     ]
    }
   ],
   "source": [
    "total_bottles = int(input(\"Enter total water bottles: \"))\n",
    "daily_drink = int(input(\"Enter bottles you drink per day: \"))\n",
    "\n",
    "day = 1\n",
    "\n",
    "while total_bottles > 0:\n",
    "    if total_bottles >= daily_drink:\n",
    "        consumed = daily_drink\n",
    "    else:\n",
    "        consumed = total_bottles\n",
    "\n",
    "    total_bottles -= consumed\n",
    "\n",
    "    print(f\"Day {day}: Drank {consumed} bottle{'s' if consumed > 1 else ''}. {total_bottles} left.\")\n",
    "    day += 1\n",
    "\n",
    "print(\"No more bottles left!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0498b3b-215e-448d-b7b3-610a234d94ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Restaurant Tip Simulator\n"
     ]
    }
   ],
   "source": [
    "print(\"Restaurant Tip Simulator\")\n",
    "bill_amount = float(input(\"Enter the total bill amount: ₹\"))\n",
    "friends = int(input(\"Enter number of friends splitting the bill: \"))\n",
    "\n",
    "# Calculate base split\n",
    "split_amount = bill_amount / friends\n",
    "print(f\"Each person pays ₹{split_amount:.2f} before tip.\")\n",
    "\n",
    "# Choose tip percentage\n",
    "print(\"\\nChoose tip percentage:\")\n",
    "print(\"1. 10%\")\n",
    "print(\"2. 20%\")\n",
    "print(\"3. 30%\")\n",
    "print(\"4. 40%\")\n",
    "print(\"5. 50%\")\n",
    "\n",
    "tip_choice = int(input(\"Enter choice (1-5): \"))\n",
    "\n",
    "# Convert choice to actual percentage\n",
    "tip_percent = tip_choice * 10\n",
    "\n",
    "tip_amount = (bill_amount * tip_percent) / 100\n",
    "total_with_tip = bill_amount + tip_amount\n",
    "final_split = total_with_tip / friends\n",
    "\n",
    "print(f\"\\n Tip selected: {tip_percent}%\")\n",
    "print(f\"Tip amount: ₹{tip_amount:.2f}\")\n",
    "print(f\"Total bill with tip: ₹{total_with_tip:.2f}\")\n",
    "print(f\"Each person pays ₹{final_split:.2f} including tip.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bbf2fb2-d1ac-451b-8af9-1529592305eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select operation:\n",
      "1. Add\n",
      "2. Subtract\n",
      "3. Multiply\n",
      "4. Divide\n"
     ]
    }
   ],
   "source": [
    "def divide(x, y):\n",
    "    if y == 0:\n",
    "        return \"Error: Division by zero\"\n",
    "    return x / y\n",
    "\n",
    "def main():\n",
    "    print(\"Select operation:\")\n",
    "    print(\"1. Add\")\n",
    "    print(\"2. Subtract\")\n",
    "    print(\"3. Multiply\")\n",
    "    print(\"4. Divide\")\n",
    "\n",
    "    choice = input(\"Enter choice (1/2/3/4): \")\n",
    "\n",
    "    if choice not in ('1', '2', '3', '4'):\n",
    "        print(\"Invalid input\")\n",
    "        return\n",
    "\n",
    "    try:\n",
    "        num1 = float(input(\"Enter first number: \"))\n",
    "        num2 = float(input(\"Enter second number: \"))\n",
    "    except ValueError:\n",
    "        print(\"Invalid number\")\n",
    "        return\n",
    "\n",
    "    if choice == '1':\n",
    "        print(f\"{num1} + {num2} = {add(num1, num2)}\")\n",
    "    elif choice == '2':\n",
    "        print(f\"{num1} - {num2} = {subtract(num1, num2)}\")\n",
    "    elif choice == '3':\n",
    "        print(f\"{num1} * {num2} = {multiply(num1, num2)}\")\n",
    "    elif choice == '4':\n",
    "        print(f\"{num1} / {num2} = {divide(num1, num2)}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afb4b47b-e995-4eef-ab6c-80bfc5faf8af",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
