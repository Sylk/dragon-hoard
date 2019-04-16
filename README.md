  
![alt](./assets/logo_desc.PNG)  

# Initial Run

On first run this bot will scrape all users from your server and give them all a balance of 1000 credits that are currently only usable on the server that the bot is running on.

# Commands

**`request`**   
TODO: description of request
```
!credits request username amountOfCredits
```
---- 
**`give`**  
TODO: description of give
```
!credits give username amountOfCredits
```
---- 

**`destroy`**  
TODO: description of destroy  
```
!credits destroy amountOfCredits
```
---- 

**`rob`**  
TODO: description of rob
```
!credits rob username amountOfCredits
```
---- 


# Setup  

**install discord.py**  
Dragon hoard runs on forked version of version of `discord.py` referred to as "the rewrite". 
which has must have pip installed to use. Then you can run the following command to get `discord.py`:    

https://pip.pypa.io/en/stable/installing/

```
python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite
```
  
  
**private key**    
In `private_key.py`, find and replace `token` with your discord token. 
  
```
nano private_key.py
```

``` 

private_key 

```

