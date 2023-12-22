#Purpose: to track ship movement.
#load packages
library(shiny)
library(leaflet)

#load data
ais<-read.csv("C:/Users/627581/Documents/AIS_Norway/ais_201801.csv", header = TRUE, sep = ";")
# Define UI for application 
ui <- fluidPage(

    # Application title
    titlePanel("Map of path travelled by ship"),

        # Show a plot of the generated distribution
        mainPanel(
          #dropdown list of ships
          uiOutput("ship_select"),
          
          #Map
          leafletOutput("locations")
           
        )
    
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  #create dropdown list
  output$ship_select<- renderUI({
    selectInput("pick_ship", "Choose a ship:", choices =c(unique(ais$mmsi)))
    
    
  })
  
  #create map
  output$locations<- renderLeaflet({
    #update map
    filtered=subset(ais, ais$mmsi==input$pick_ship)
    
    
    #setup map
    locations<-leaflet(data=filtered)
    locations<-addTiles(locations)
    locatoins<-setView(locations, lng=9.76, lat=59.01, zoom=14)
    r<-nrow(filtered)
    x<-1/r
    y<-0
    for (i in 0:r){
    y<-y+x
    
    locations<-addCircles(locations, lng=~lon[i], lat=~lat[i], color = "red",fillColor = "green",opacity = y, fillOpacity = y)
    
    
    }
    locations
    
  })
}

# Run the application 
shinyApp(ui = ui, server = server)
