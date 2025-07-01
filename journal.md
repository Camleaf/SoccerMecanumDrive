---
title: "Mechmania 2024/25 soccer bot"
author: "Camleaf"
description: "A robot meant to play the 2024/25 Mechmania soccer challenge"
created_at: "2025-06-28"
---

# June 29th:

Time to get started!!
Like the previous project I did for Highway, I will be using 6V 300rpm JGB37-520 Motors,BTS7960 motor drivers. I think this time I'll try something new and use a ESP32 to connect to a playstation controller.

This project, I am planning on making a bot which can play the soccer 2024/25 game for Mechmania, a regional robotics competition that may be a little hard to find online. The game consists of collecting and scoring balls by pushing them into a lowered net or a raised net. I intend to make a mecanum wheel drivetrain with two distinct mechanisms; Intake, which grabs balls off the ground and stores it in the robot, and a servo-controlled arm which grabs them and raises them onto the highest scoring platform.


To start, I CADded out a small drivetrain.

<img src='./JOURNAL_IMG/CAD drivebase.png' width='500'>

Unfortunately, due to the fact that my 3D printer can only print 250mm by 210mm, I had to split the drivetrain into two distinct pieces, 240mm by 150mm. The end frame is 240m by 300mm, and has a slight rectangular design, although the wheel placements are about square.

I also couldn't find a suitable 60mm Mecanum wheel reference model which matched the specs of the ones I'm looking at for this project, so I made some grey cylinders for testing purposes.

To make use of the empty middle section, I added some motor driver mounts, as they take up a lot of space normally and this is a perfect spot to add them. I also used some BTS7960 references for accurate construction.

<img src='./JOURNAL_IMG/CAD drivebase_drivers.png' width='500'>


Since the bottom area is now done, I will move on to the middle layer, this layer will hold all the batteries, and the microprocessor.

<img src='./JOURNAL_IMG/CAD middle_layer.png' width='500'>

I left some spaces for the wheels to get a more compact fit, and I left a big hole in the centre of the car to have easier access to all the motor drivers at the base should anything break. 
One of the main pillars I'm trying to go for for this car is ease of maintenance.


From there, I added a top section to the CAD model, which later i will start to add the intake and robotic arm mechanisms to.

<img src='./JOURNAL_IMG/CAD top_layer_proto.png' width='500'>

From here, I've been Cadding out stuff since this morning, at it's 6pm, so I'm going to call this a night and get back to working on this tomorrow.


**Total Time Spent 6h**


# June 30th:

Ok, so now that I have the top section in, I'm going to start building the intake. To start, I created an inramp that leads to the top of the frame.


<img src='./JOURNAL_IMG/CAD_inramp.png' width='500'>