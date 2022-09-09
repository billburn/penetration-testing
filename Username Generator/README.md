# Username Generation Tools

## Username_Generator
As an example, maybe we want to create a wordlist from these names to try differnt combinations

```
{first name}: john
{last name}: smith
{first name}{last name}:  johnsmith 
{last name}{first name}:  smithjohn  
first letter of the {first name}{last name}: jsmith 
first letter of the {last name}{first name}: sjohn  
first letter of the {first name}.{last name}: j.smith 
first letter of the {first name}-{last name}: j-smith
```

```
echo "John Smith" > users.lst
python3 username_generator.py -w users.lst

john
smith
j.smith
j-smith
j_smith
j+smith
jsmith
smithjohn
```

[username_generator](https://github.com/therodri2/username_generator.git)