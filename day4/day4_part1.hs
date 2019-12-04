-- Day 4: Secure Container
-- Part 1

-- Turns a number into a list of digits
digit :: Int -> [Int]
digit 0 = []
digit x = digit (x `div` 10) ++ [x `mod` 10]

-- Checks for two equal adjacent numbers
adjacent :: [Int] -> Bool
adjacent (x:[]) = False
adjacent (x:y:xs) = x == y || adjacent (y:xs)

-- Checks that from left to right the digits never decrease
crescent :: [Int] -> Bool
crescent (x:[]) = True
crescent (x:y:xs) = x <= y && crescent (y:xs)

-- Counts the cases that match the criteria within the given range
passwords :: Int -> Int -> Int
passwords x y = length [a | a <- [x..y], adjacent (digit a), crescent(digit a)]
