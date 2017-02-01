Cover: 
1) difference between window.onload() and jquery $(document).ready. window.onload is valid when all the images are loaded. jquery document ready true when dom loaded and images not yet all loaded
2) adding event listeners and coordinate system for clientX, clientY relative to window/browser and div element



1) TestChrome.html plays video works in Firefox not in Chrome. To test open in pycharm right click open in browser select Firefox or Chrome
2) TestImageDraw.html broken. 
3) TestImageDraw2.html doesnt do shit
4) testmousedown.html: display mouse coordinates in left div, test event bubbling/capture
5) testmousepos.html: display mouse coordinates in div. What is diff w/above? Less code. 
6) TestVideoSource. bottom is color image top is grayscale image. 
7) test_canvas_greenline.html write green line to canvas w/fill for image. Simplest case for debugging
   test_canvasgreenlinevideo.html green line to video image. For debugging reference. Comment out requestAnimationFrame(); Mouse click draws green line on canvas
   test_canvasredvideo.html draw red line where mouse click is. use red line b/c it is easier to see. Especially if mouse coordinates don't match. 
   To debug the x y coordinates for mouse click on canvas. The webposts are all wrong
   1) draw a 100px line on the screen on a mouse click in a fixed position. 0,0 is the easiest
   2) try to get the x or y coordinate right first. click and you should see a horizontal Y coordinate matching the Y coordinate of the mouse
      this simple exercise shows that e.clientX*e.clientY is wrong. And e.clientX*4 and e.clientY*4 is wrong
      you get: X=some constant and Y=(canvas.width*4)*y where y = e.clientY-rect.top
      Once Y fixed, modify X.
      This is in file test_canvasredvideo_y.html
   3) test_canvasredvideo.html shows 100px red line display to canvas w/ X * & Y coordinate calculation
 
8) 2canvas.html draw rectangle onto canvas. Simplest case for debugging. 
9) test_requestanimationframe.html. Shouldnt use setTimeout like in TestVideoSource should use requestAnimationFrame
which is controlled by browser v.s. guessing when next frame is ready by timeout. 

