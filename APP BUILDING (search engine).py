#============SEARCH ENGINE============


import wikipedia as w
import webbrowser as wb

w.set_user_agent("MyWikipediaSearchApp/1.0 (contact: janaaspectre@gmail.com)")

heading = "============= welcome to search engine ============="
print(heading.title())
INPUT = input("search:  ")
results = w.search(INPUT)

if len(results) == 0:
    print("no results found")
else:
    print("\nRESULTS:")
    for i in range(len(results)):
        print(i+1,".",results[i])
while True:
        choice = int(input("\nchose result number:  "))
        if 1<= choice<= len(results):
            break
        elif choice<1:
            print("the number is too low.please choose a valid result")
        else:
            print("the number is too high.choose a valid result")

selected = results[choice - 1]
print("\nSummary\n")

    
try:
    print(w.summary(selected))
    page = w.page(selected)
    print("\nOppening full artical in browser: {page.url}")
    wb.open(page.url)
        
except w.exceptions.PageError:
    print("page not found!!!")
        
except w.exceptions.DisambiguationError as e:
    print("multiple pages found:")
    print(e.options[:10])
    
        


    
    
    
    

            
            
    
   






