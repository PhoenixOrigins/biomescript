def main():
    print("------------------------")
    print("Biomes Utility | jstnf")
    print("Phoenix Origins")
    print("------------------------")

    biome_file = open("biomes.csv", "r")
    biome_lines = biome_file.readlines()
    biome_file.close()

    biome_conf = open("config.yml", "w+", newline = "")
    biome_conf.write("biomes:\n")
    biome_conf.write("  biomesList:\n")

    for line in biome_lines:
      sections = line.split(',')
      biome_conf.write("    %s:\n" % sections[0].lower())
      biome_conf.write("      friendlyName: '%s'\n" % sections[1])
      biome_conf.write("      description: '%s'\n" % sections[2])
      biome_conf.write("      icon: '%s'\n" % sections[3].rstrip())
      biome_conf.write("      islandLevel: 0\n")
      biome_conf.write("      cost: 50\n")
    biome_conf.close()

if __name__ == "__main__":
  main()