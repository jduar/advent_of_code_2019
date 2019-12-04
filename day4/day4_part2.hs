-- Day 4: Secure Container
-- Part 2

-- The difference to part 1 is that we need to make sure that the two equal
-- adjacent digits aren't part of a larger number of equal digits:
-- 123444 doesn't count; 111122 counts because the 22 isn't part of a larger
-- number.

import Data.List

-- Turns a number into a list of digits
digit :: Int -> [Int]
digit 0 = []
digit x = digit (x `div` 10) ++ [x `mod` 10]

-- We group equal adjacent elements, map the groups' lengths and check if
-- one of the groups has length 2 - meaning exactly two adjacent equal digits.
adjacent :: [Int] -> Bool
adjacent x = elem 2 (map length (group x))

-- Checks that from left to right the digits never decrease
crescent :: [Int] -> Bool
crescent (x:[]) = True
crescent (x:y:xs) = x <= y && crescent (y:xs)

-- Counts the cases that match the criteria within the given range
passwords :: Int -> Int -> Int
passwords x y = length [a | a <- [x..y], adjacent (digit a), crescent(digit a)]
