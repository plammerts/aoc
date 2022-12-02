input =
  File.read!("day6.txt")
  |> String.split(",")
  |> Enum.map(&String.to_integer(&1))
  |> Enum.reduce(List.duplicate(0, 9), fn number, acc ->
    List.update_at(acc, number, &(&1 + 1))
  end)

Enum.reduce(1..80, input, fn _, [head | tail] ->
  new_list = tail ++ [head]

  List.update_at(new_list, 6, &(&1 + head))
end)
|> Enum.sum()
|> IO.inspect()
