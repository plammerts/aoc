positions =
  File.read!("day7.txt")
  |> String.split(",")
  |> Enum.map(&String.to_integer(&1))

max_pos = Enum.max(positions)

Enum.reduce(0..max_pos, nil, fn outcome, outcome_acc ->
  total_fuel =
    Enum.reduce(positions, 0, fn pos, acc ->
      diff = abs(outcome - pos)
      acc + div(diff * (diff + 1), 2)
    end)

  case outcome_acc do
    nil -> total_fuel
    outcome_acc -> if total_fuel < outcome_acc, do: total_fuel, else: outcome_acc
  end
end)
|> IO.inspect()
