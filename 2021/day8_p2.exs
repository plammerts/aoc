defmodule Day8 do
  def find_mapping(entry) do
    mapping = %{
      1 => nil,
      2 => nil,
      3 => nil,
      4 => nil,
      5 => nil,
      6 => nil,
      7 => nil,
      8 => nil,
      9 => nil
    }

    num_mapping =
      Enum.reduce(entry, mapping, fn e, m ->
        case MapSet.size(e) do
          2 ->
            Map.replace!(m, 1, e)

          3 ->
            Map.replace!(m, 7, e)

          4 ->
            Map.replace!(m, 4, e)

          7 ->
            Map.replace!(m, 8, e)

          _ ->
            m
        end
      end)
      |> IO.inspect()

    seg_mapping = [a: nil, b: nil, c: nil, d: nil, e: nil, f: nil, g: nil]

    {seg_mapping, num_mapping} =
      {seg_mapping, num_mapping}
      |> map_a(entry)
      |> map_g(entry)
      |> IO.inspect()
  end

  def map_a({seg_mapping, num_mapping}, _entry) do
    seg =
      MapSet.difference(Map.fetch!(num_mapping, 7), Map.fetch!(num_mapping, 1))
      |> MapSet.to_list()
      |> hd()

    seg_mapping = Keyword.replace!(seg_mapping, :a, seg)
    {seg_mapping, num_mapping}
  end

  def map_g({seg_mapping, num_mapping}, entry) do
    uni = MapSet.union(Map.fetch!(num_mapping, 4), Map.fetch!(num_mapping, 7))

    {e, seg} =
      Enum.find_value(entry, fn e ->
        diff = MapSet.difference(e, uni)

        if MapSet.size(diff) == 1 do
          {e, diff |> MapSet.to_list() |> hd()}
        end
      end)

    seg_mapping = Keyword.replace!(seg_mapping, :g, seg)
    num_mapping = Map.replace!(num_mapping, 9, e)
    {seg_mapping, num_mapping}
  end

  def map_e({seg_mapping, num_mapping}, entry) do
    seg_9 = Map.fetch!(num_mapping, 9)

    {e, seg} =
      Enum.find_value(entry, fn e ->
        # TODO: check of verschil tussen 9 en e 1ntje is en of die seg niet voorkomt in 1,4,7
        diff = MapSet.difference(e, uni) |> IO.inspect(label: :diff)

        if MapSet.size(diff) == 1 do
          {e, diff |> MapSet.to_list() |> hd()}
        end
      end)

    seg_mapping = Keyword.replace!(seg_mapping, :g, seg)
    num_mapping = Map.replace!(num_mapping, 9, e)
    {seg_mapping, num_mapping}
  end
end

outputs =
  File.stream!("day8.txt")
  |> Enum.map(fn line ->
    [entry, output] =
      line
      |> String.split("|")

    entry =
      entry
      |> String.trim()
      |> String.split(" ")
      |> Enum.map(&(String.split(&1, "", trim: true) |> MapSet.new()))

    output =
      output
      |> String.trim()
      |> String.split(" ")
      |> Enum.map(&(String.split(&1, "", trim: true) |> MapSet.new()))

    {entry, output}
  end)
  |> IO.inspect()

mappings = Enum.map(outputs, fn {entry, output} -> Day8.find_mapping(entry) end)
