
# a deck of cards is always fifty-two 

def faro(deck: list[str]) -> list[str]:
    res = []

    for i in range(26):
        res.append(deck[i])
        res.append(deck[i + 26])
    
    return res

newDeckOrder = [
  'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
  'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
  'KC', 'QC', 'JC', '10C', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C', 'AC',
  'KH', 'QH', 'JH', '10H', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H', 'AH']

firstFaro = faro(newDeckOrder)
print(firstFaro == [
  'AS', 'KC', '2S', 'QC', '3S', 'JC', '4S', '10C', '5S', '9C', '6S', '8C', '7S',
  '7C', '8S', '6C', '9S', '5C', '10S', '4C', 'JS', '3C', 'QS', '2C', 'KS', 'AC',
  'AD', 'KH', '2D', 'QH', '3D', 'JH', '4D', '10H', '5D', '9H', '6D', '8H', '7D',
  '7H', '8D', '6H', '9D', '5H', '10D', '4H', 'JD', '3H', 'QD', '2H', 'KD', 'AH'])

secondFaro = faro(firstFaro)
print(secondFaro == [
  'AS', 'AD', 'KC', 'KH', '2S', '2D', 'QC', 'QH', '3S', '3D', 'JC', 'JH', '4S',
  '4D', '10C', '10H', '5S', '5D', '9C', '9H', '6S', '6D', '8C', '8H', '7S', '7D',
  '7C', '7H', '8S', '8D', '6C', '6H', '9S', '9D', '5C', '5H', '10S', '10D', '4C',
  '4H', 'JS', 'JD', '3C', '3H', 'QS', 'QD', '2C', '2H', 'KS', 'KD', 'AC', 'AH'])

thirdFaro = faro(secondFaro)
print(thirdFaro == [
  'AS', '7C', 'AD', '7H', 'KC', '8S', 'KH', '8D', '2S', '6C', '2D', '6H', 'QC',
  '9S', 'QH', '9D', '3S', '5C', '3D', '5H', 'JC', '10S', 'JH', '10D', '4S', '4C',
  '4D', '4H', '10C', 'JS', '10H', 'JD', '5S', '3C', '5D', '3H', '9C', 'QS', '9H',
  'QD', '6S', '2C', '6D', '2H', '8C', 'KS', '8H', 'KD', '7S', 'AC', '7D', 'AH'])

fourthFaro = faro(thirdFaro)
print(fourthFaro == [
  'AS', '4D', '7C', '4H', 'AD', '10C', '7H', 'JS', 'KC', '10H', '8S', 'JD', 'KH',
  '5S', '8D', '3C', '2S', '5D', '6C', '3H', '2D', '9C', '6H', 'QS', 'QC', '9H',
  '9S', 'QD', 'QH', '6S', '9D', '2C', '3S', '6D', '5C', '2H', '3D', '8C', '5H',
  'KS', 'JC', '8H', '10S', 'KD', 'JH', '7S', '10D', 'AC', '4S', '7D', '4C', 'AH'])

fifthFaro = faro(fourthFaro)
print(fifthFaro == [
  'AS', '9S', '4D', 'QD', '7C', 'QH', '4H', '6S', 'AD', '9D', '10C', '2C', '7H',
  '3S', 'JS', '6D', 'KC', '5C', '10H', '2H', '8S', '3D', 'JD', '8C', 'KH', '5H',
  '5S', 'KS', '8D', 'JC', '3C', '8H', '2S', '10S', '5D', 'KD', '6C', 'JH', '3H',
  '7S', '2D', '10D', '9C', 'AC', '6H', '4S', 'QS', '7D', 'QC', '4C', '9H', 'AH'])

sixthFaro = faro(fifthFaro)
print(sixthFaro == [
  'AS', '5S', '9S', 'KS', '4D', '8D', 'QD', 'JC', '7C', '3C', 'QH', '8H', '4H',
  '2S', '6S', '10S', 'AD', '5D', '9D', 'KD', '10C', '6C', '2C', 'JH', '7H', '3H',
  '3S', '7S', 'JS', '2D', '6D', '10D', 'KC', '9C', '5C', 'AC', '10H', '6H', '2H',
  '4S', '8S', 'QS', '3D', '7D', 'JD', 'QC', '8C', '4C', 'KH', '9H', '5H', 'AH'])

seventhFaro = faro(sixthFaro)
print(seventhFaro == [
  'AS', '3S', '5S', '7S', '9S', 'JS', 'KS', '2D', '4D', '6D', '8D', '10D', 'QD',
  'KC', 'JC', '9C', '7C', '5C', '3C', 'AC', 'QH', '10H', '8H', '6H', '4H', '2H',
  '2S', '4S', '6S', '8S', '10S', 'QS', 'AD', '3D', '5D', '7D', '9D', 'JD', 'KD',
  'QC', '10C', '8C', '6C', '4C', '2C', 'KH', 'JH', '9H', '7H', '5H', '3H', 'AH'])

eighthFaro = faro(seventhFaro)
print(eighthFaro == [
  'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
  'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
  'KC', 'QC', 'JC', '10C', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C', 'AC',
  'KH', 'QH', 'JH', '10H', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H', 'AH'])

print("Was the original order preserved after 8 shuffles? ",
      "Yes" if newDeckOrder == eighthFaro else "No")
