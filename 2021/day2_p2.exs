%{horizontal: horizontal, depth: depth} =
  File.stream!("day2.txt")
  |> Enum.reduce(%{horizontal: 0, depth: 0, aim: 0}, fn line, acc ->
    [command, value] = String.split(line)
    value = String.to_integer(value)

    case command do
      "forward" ->
        acc
        |> Map.update!(:horizontal, &(&1 + value))
        |> Map.update!(:depth, &(&1 + acc.aim * value))

      "down" ->
        Map.update!(acc, :aim, &(&1 + value))

      "up" ->
        Map.update!(acc, :aim, &(&1 - value))
    end
  end)

IO.inspect(horizontal * depth)
