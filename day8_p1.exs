outputs =
  File.stream!("day8.txt")
  |> Enum.map(fn line ->
    [_entry, output] =
      line
      |> String.split("|")

    output |> String.trim() |> String.split(" ")
  end)

Enum.reduce(outputs, 0, fn output, acc1 ->
  acc1 +
    Enum.reduce(output, 0, fn o, acc2 ->
      if String.length(o) in [2, 3, 4, 7] do
        acc2 + 1
      else
        acc2
      end
    end)
end)
|> IO.inspect()
