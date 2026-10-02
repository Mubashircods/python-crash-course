from pathlib import Path

lines = 'I love Python Programing.\n'
lines += 'I also love to Developed softwear.\n'
lines += "One day I'll ne developed a unique and major softwear.\n"
write = Path("write_by_python.txt")
write.write_text(lines)
