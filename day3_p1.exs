numbers =
  File.stream!("day3.txt")
  |> Enum.map(&(&1 |> String.trim() |> String.split("", trim: true)))

length = numbers |> hd() |> length()
accumulator = List.duplicate({0, 0}, length)

{gamma, epsilon} =
  numbers
  |> Enum.reduce(accumulator, fn values, acc ->
    Enum.zip(values, acc)
    |> Enum.map(fn {v, {acc1, acc2}} ->
      case v do
        "0" -> {acc1 + 1, acc2}
        "1" -> {acc1, acc2 + 1}
      end
    end)
  end)
  |> Enum.reduce({"", ""}, fn {num_zeroes, num_ones}, {gamma, epsilon} ->
    if num_zeroes > num_ones do
      {gamma <> "0", epsilon <> "1"}
    else
      {gamma <> "1", epsilon <> "0"}
    end
  end)

gamma = Integer.parse(gamma, 2) |> elem(0)
epsilon = Integer.parse(epsilon, 2) |> elem(0)
IO.inspect(gamma * epsilon)
