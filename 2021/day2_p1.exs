%{horizontal: horizontal, depth: depth} =
  File.stream!("day2.txt")
  |> Enum.reduce(%{horizontal: 0, depth: 0}, fn line, acc ->
    [command, value] = String.split(line)
    value = String.to_integer(value)

    case command do
      "forward" -> Map.update!(acc, :horizontal, &(&1 + value))
      "down" -> Map.update!(acc, :depth, &(&1 + value))
      "up" -> Map.update!(acc, :depth, &(&1 - value))
    end
  end)

IO.inspect(horizontal * depth)
