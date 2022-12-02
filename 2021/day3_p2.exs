defmodule Day3Part2 do
  def find([number], _bit_index, _bit_criteria),
    do: number |> Enum.join() |> Integer.parse(2) |> elem(0)

  def find(numbers, bit_index, bit_criteria) do
    filtered = bit_criteria.(numbers, bit_index)
    find(filtered, bit_index + 1, bit_criteria)
  end

  def oxygen_criteria(numbers, bit_index) do
    {zeroes, ones} =
      Enum.reduce(numbers, {0, 0}, fn number, {zeroes, ones} ->
        case Enum.at(number, bit_index) do
          0 -> {zeroes + 1, ones}
          1 -> {zeroes, ones + 1}
        end
      end)

    if zeroes > ones do
      Enum.filter(numbers, &(Enum.at(&1, bit_index) == 0))
    else
      Enum.filter(numbers, &(Enum.at(&1, bit_index) == 1))
    end
  end

  def co2_scrubber_rating(numbers, bit_index) do
    {zeroes, ones} =
      Enum.reduce(numbers, {0, 0}, fn number, {zeroes, ones} ->
        case Enum.at(number, bit_index) do
          0 -> {zeroes + 1, ones}
          1 -> {zeroes, ones + 1}
        end
      end)

    if zeroes > ones do
      Enum.filter(numbers, &(Enum.at(&1, bit_index) == 1))
    else
      Enum.filter(numbers, &(Enum.at(&1, bit_index) == 0))
    end
  end
end

numbers =
  File.stream!("day3.txt")
  |> Enum.map(fn line ->
    line
    |> String.trim()
    |> String.split("", trim: true)
    |> Enum.map(&String.to_integer(&1))
  end)

oxygen = Day3Part2.find(numbers, 0, &Day3Part2.oxygen_criteria/2)
co2_scrubber = Day3Part2.find(numbers, 0, &Day3Part2.co2_scrubber_rating/2)
IO.inspect(oxygen * co2_scrubber)
