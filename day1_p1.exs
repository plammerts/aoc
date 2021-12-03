File.stream!("day1.txt")
|> Stream.map(&(&1 |> String.trim() |> String.to_integer()))
|> Stream.chunk_every(3, 1)
|> Enum.reduce(0, fn chunked_list, acc ->
  increased =
    case chunked_list do
      [prev, next, _] ->
        next > prev

      [prev, next] ->
        next > prev
    end

  if increased, do: acc + 1, else: acc
end)
|> IO.inspect()
