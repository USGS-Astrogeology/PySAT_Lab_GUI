#include "guitest.h"
#include "ui_guitest.h"
#include <QString>
#include <QFile>
#include <QDir>
#include <QMessageBox>
#include <QFileDialog>
#include <QDebug>
#include <QRect>
#include <QDesktopWidget>

//Global variables
int norm_push = 0;      // this variable measures how many time's the normalization button has been pushed
int norm_size = 7;      // this variable measures the size of arrays in the normalization section

GuiTest::GuiTest (QWidget *parent):
    QMainWindow(parent), ui(new Ui::GuiTest){
    ui->setupUi(this);
    //TODO: fix sizing issues, this will allow any computer to have a nicely sized window
    QRect rect = QApplication::desktop()->screenGeometry();
    int height = rect.height();
    this->resize(this->width(), height*0.9);
    for (int i = 0; i < norm_size; i++){
        setSpinleftVisible(i, false);
        setSpinrightVisible(i, false);
        setLabelsVisible(i, false);
    }


}

GuiTest::~GuiTest(){
    delete ui;
}

/*
 *
 *           |--------------------------------------- this is a label it doesn't do anything
 *           |        |------------------------------ this value will be spinleft it will have values ranging from 0 to 99
 *           |        |            |----------------- this value will be spinright it will have values ranging from 0 to 99
 *           v        v            v
 *    |-------------------------------------------|
 *    |    value1 [         ] [         ]         | <- There are 8 of each; label, spinleft, spinright.
 *    |                         add value         | <- each of these fields are hidden until the user hits the add value button
 *    |                                           | -> Personal Note: Check to see if the user has increased "push++"
 *    |                                           |    if they had, then take the values entered in the boxes and write it to the
 *    |-------------------------------------------|    python file.
 *
 *    TODO: add the ability to show buttons for normalization these are a bunch of lists that parse
 *    each item and then will be setVisibile to false so they aren't there until you click a button
 */

/*************** GUI Interface **************
 *     |-----------------------------------|
 *     |   Maskfile               [..]     | <- on_toolButton_clicked  ; this will open a dialog to look for the .csv mask file
 *     |   Unknown Data           [..]     | <- on_toolButton_2_clicked; this will open a dialog to look for the .csv unknown data file
 *     |   Full Database          [..]     | <- on_toolButton_3_clicked; this will open a dialog to look for the .csv full database file
 *     |   Output Location        [..]     | <- on_toolButton_4_clicked; this will open a dialog to look for a directory that you'd like
 *     |                                   |                             to output your images to
 *     |                                   |
 *     .                                   .
 *     .                            [ok]   . <- on_pushButton_clicked; this will create the final py file
 *     |-----------------------------------|
 *
 */


void GuiTest::setLabelsVisible(int index, bool visible){
    QLabel* labels[norm_size] = {ui->norm_label_2,
                            ui->norm_label_3,
                            ui->norm_label_4,
                            ui->norm_label_5,
                            ui->norm_label_6,
                            ui->norm_label_7,
                            ui->norm_label_8};
    labels[index]->setVisible(visible);
}

void GuiTest::setSpinrightVisible(int index, bool visible){
    QSpinBox* spinright[norm_size] = {ui->norm_spinBox_2,
                                 ui->norm_spinBox_3,
                                 ui->norm_spinBox_4,
                                 ui->norm_spinBox_5,
                                 ui->norm_spinBox_6,
                                 ui->norm_spinBox_7,
                                 ui->norm_spinBox_8};
    spinright[index]->setVisible(visible);
}

void GuiTest::setSpinleftVisible(int index, bool visible){
    QSpinBox* spinleft[norm_size] = {ui->norm_spinBox_10,
                                ui->norm_spinBox_11,
                                ui->norm_spinBox_12,
                                ui->norm_spinBox_13,
                                ui->norm_spinBox_14,
                                ui->norm_spinBox_15,
                                ui->norm_spinBox_16};
    spinleft[index]->setVisible(visible);
}

void GuiTest::on_toolButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Open New File", QDir::homePath());
    ui->lineEdit->setText(file_name);
}

void GuiTest::on_toolButton_2_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Open New File", QDir::homePath());
    ui->lineEdit_2->setText(file_name);
}

void GuiTest::on_toolButton_3_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Open New File", QDir::homePath());
    ui->lineEdit_3->setText(file_name);
}

void GuiTest::on_toolButton_4_clicked(){
    const QString &file_name = QFileDialog::getExistingDirectory(this, "Open New Directory", QDir::homePath());
    ui->lineEdit_4->setText(file_name);
}

void GuiTest::on_actionExit_triggered(){
    this->close();
}

/*************** GUI Interface **************/

void GuiTest::on_pushButton_13_clicked(){
    if (norm_push >= norm_size){
        QMessageBox::critical(this, "Warning", "Cannot add anymore values");
    } else {
        setSpinleftVisible(norm_push, true);
        setSpinrightVisible(norm_push, true);
        setLabelsVisible(norm_push, true);
        norm_push++;
    }
    //TODO: When a button is pressed, two value boxes appear, have those values from these boxes added into the file.
    //BUT only when the button has been pressed!

}

void GuiTest::on_pushButton_clicked(){

}

void GuiTest::on_norm_spinBox_9_valueChanged(int arg1)
{
    qDebug() << arg1;
}

void GuiTest::on_norm_spinBox_valueChanged(int arg1)
{
    qDebug() << arg1;
}
