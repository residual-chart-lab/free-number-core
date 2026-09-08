function Table(t)
  if #t.colspecs == 2 and #t.head.rows > 0 then
    local first = pandoc.utils.stringify(t.head.rows[1].cells[1].contents)
    if first == 'Note' then
      t.colspecs = {{pandoc.AlignLeft, 0.10}, {pandoc.AlignLeft, 0.90}}
    end
  end
  return t
end
